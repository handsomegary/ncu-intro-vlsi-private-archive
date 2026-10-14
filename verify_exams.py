"""Public exam artifacts and analytical checks; optional private-source integrity.

Set VLSI_PRIVATE_ORIGINALS to a private archive root to verify original PDFs
under exams/YYYY/term/. Known hashes may be recorded in PRIVATE_SOURCES.json
(assets with path/sha256/bytes), coverage, source metadata, or saved PDF QA.
Without that variable, private-source integrity is explicitly not_run.
"""
from pathlib import Path
import csv,hashlib,json,math,os,re
ROOT=Path(__file__).resolve().parent
P=ROOT/'exams'/'2024'/'midterm'
def need(ok,msg):
    if not ok:raise AssertionError(msg)
def js(name):return json.loads((P/name).read_text(encoding='utf-8-sig'))
def rows(name):
    with (P/name).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))

def read_json(path):
    return json.loads(path.read_text(encoding='utf-8-sig'))

def private_assets():
    """Read portable metadata only; this never opens a private source file."""
    manifest=ROOT/'PRIVATE_SOURCES.json'
    if not manifest.is_file():return {}
    data=read_json(manifest)
    need(isinstance(data.get('assets'),list),'Private asset metadata must contain an assets list')
    result={}
    for asset in data['assets']:
        name=asset['path'].replace('\\','/')
        need(name not in result,'Duplicate private asset metadata path')
        result[name]=asset
    return result

def original_relative(item):
    expected='exams/{}/{}/original-exam.pdf'.format(item['year'],item['exam'])
    declared=item.get('private_original_path',expected).replace('\\','/')
    need(declared==expected,'Private original path must match its exam year and term')
    return expected

def original_hash_record(item,folder,assets):
    """Use a recorded original-file digest, never the digest being tested."""
    relative=original_relative(item)
    if relative in assets:return assets[relative]
    for source in [item,read_json(folder/'sources.json')]:
        for key in ['private_original_sha256','original_exam_sha256','original_copy_sha256','original_sha256']:
            if source.get(key):return {'sha256':source[key]}
    # Legacy packages use several QA schemas. Match the original's filename,
    # rather than a source-container hash that may include student answer pages.
    for name in ['pdf_qa.json','qa.json','visual-qa.json','qa_summary.json']:
        path=folder/name
        if not path.is_file():continue
        data=read_json(path)
        for key in ['artifact_sha256','artifact_hashes','sha256','stable_file_sha256']:
            value=data.get(key,{})
            if isinstance(value,dict) and value.get('original-exam.pdf'):
                return {'sha256':value['original-exam.pdf']}
        for record in data.get('records',[]):
            if record.get('file')=='original-exam.pdf' and record.get('sha256'):
                return {'sha256':record['sha256']}
    raise AssertionError('Missing known SHA-256 for '+relative)

def private_integrity(coverage):
    value=os.environ.get('VLSI_PRIVATE_ORIGINALS','').strip()
    if not value:
        return {'status':'not_run','reason':'VLSI_PRIVATE_ORIGINALS is not set',
                'original_PDFs_checked':0,'CSV_image_streams_checked':0}
    private_root=Path(value).expanduser().resolve()
    need(private_root.is_dir(),'Configured private archive root is unavailable')
    assets=private_assets()
    pdf_count=stream_count=0
    for item in coverage['completed_exams']:
        folder=ROOT/'exams'/str(item['year'])/item['exam']
        relative=original_relative(item)
        original=(private_root/relative).resolve()
        need(original.is_relative_to(private_root),'Private original must remain inside its configured root')
        need(original.is_file(),'Missing private source: '+relative)
        raw=original.read_bytes()
        need(raw.startswith(b'%PDF-'),'Invalid private PDF: '+relative)
        known=original_hash_record(item,folder,assets)
        expected=str(known.get('sha256','')).lower()
        need(re.fullmatch(r'[0-9a-f]{64}',expected) is not None,'Invalid known SHA-256 for '+relative)
        need(hashlib.sha256(raw).hexdigest()==expected,'Private PDF SHA-256 mismatch: '+relative)
        if known.get('bytes') is not None:
            need(len(raw)==int(known['bytes']),'Private PDF byte count mismatch: '+relative)
        pdf_count+=1
        # These CSVs record exact source/embedded JPEG bytes, not mathematical
        # outputs. Verify them against the configured private PDF only.
        integrity_tables=sorted(folder.glob('original*integrity*.csv'))
        if integrity_tables:
            from pypdf import PdfReader
            pages=PdfReader(original).pages
            for table in integrity_tables:
                with table.open(encoding='utf-8-sig',newline='') as handle:
                    evidence=list(csv.DictReader(handle))
                need(bool(evidence),'Empty original-image integrity evidence')
                for row in evidence:
                    number=int(row.get('page',row.get('panel',0)))
                    need(1<=number<=len(pages),'Private image page index outside its original PDF')
                    objects=pages[number-1]['/Resources']['/XObject'].get_object().values()
                    images=[obj.get_object() for obj in objects if obj.get_object().get('/Subtype')=='/Image']
                    need(len(images)==1,'Expected one recorded JPEG per private source page')
                    image=images[0].get_data()
                    digest=hashlib.sha256(image).hexdigest()
                    for key in ['source_sha256','embedded_sha256']:
                        need(digest==row[key].lower(),'Private embedded JPEG SHA-256 mismatch: '+relative)
                    size=row.get('bytes',row.get('JPEG_bytes'))
                    if size:need(len(image)==int(size),'Private embedded JPEG byte count mismatch: '+relative)
                    stream_count+=1
    return {'status':'passed','original_PDFs_checked':pdf_count,
            'CSV_image_streams_checked':stream_count}
def verify_2024_midterm():
    for name in ['exam.pdf','solution.pdf']:
        need((P/name).read_bytes().startswith(b'%PDF-'),'Missing exam PDF')
    for name in ['exam.tex','solution.tex']:
        tex=(P/name).read_text(encoding='utf-8')
        need('\\begin{document}' in tex and '\\end{document}' in tex,'Standalone TeX')
        need('\\includegraphics' not in tex and '\\input{' not in tex,'Editable standalone reconstruction')
    s=js('sources.json');need(s['published_original_exam_pages']==[1,2] and s['local_reviewed_handwritten_answer_pages']==[3,4,5,6],'Source partition')
    need(sum(s['question_points'])==100 and sum(s['question_1_part_points'])==30,'Original point totals')
    q=js('q2_q7_verification.json');need(q['status']=='PASS','Logic status')
    a=rows('q2_mux_truth.csv');need(len(a)==16,'MUX coverage')
    seen=set()
    for r in a:
        s,x,y,z=(int(r[k]) for k in ['s','x','y','z']);seen.add((s,x,y,z))
        expected=int((y and (x or z)) if s else (x or y or z))
        need(int(r['expected'])==int(r['mux_output'])==expected and r['passed']=='True','MUX independent cofactor check')
    need(len(seen)==16,'Unique MUX cases')
    a=rows('q7_switch_checks.csv');need(len(a)==32,'CMOS coverage')
    counts={'a':0,'b':0,'c':0}
    for r in a:
        x,y,z=(int(r[k]) for k in ['X','Y','Z']);part=r['part'];counts[part]+=1
        underlying=(x and (y or z)) if part=='a' else ((x and y) or z) if part=='b' else (x or (y and (int(r['W']) or z)))
        expected=int(not underlying)
        need(int(r['expected'])==int(r['output'])==expected and r['rail_exclusive']=='True' and r['passed']=='True','CMOS independent polarity/rail check')
    need(counts=={'a':8,'b':8,'c':16},'CMOS part coverage')
    q=js('q3_q6_verification.json')
    need(len(rows('q3_stage_checks.csv'))==40 and len(rows('q4_regions.csv'))==15 and len(rows('q5_noise_scenarios.csv'))==4,'Analytical row counts')
    for case in q['Q3']['cases'][:2]:
        b=case['best'];h=case['input_cap_over_Cg']
        need(b['total_stages_including_A']==3 and b['inserted_inverters']==2 and b['inserted_buffer_noninverting'],'Chain polarity/count')
        need(math.isclose(b['delay_T_over_R_Cg'],3*h**(1/3),rel_tol=1e-12),'Chain delay')
    need(math.isclose(q['Q4']['rising_input_switch_onset_V'],.8),'Switch-R threshold')
    need(q['Q5']['source_quantitative_noise_margins'] is None,'No invented source margins')
    original=q['Q6']['student_design_recomputed'];fixed=q['Q6']['corrected_design']
    need(original['worst_delay_over_R_Cg']==10 and not original['strictly_below_8_R_Cg'],'Student capacitance error retained')
    need(fixed['inverter_input_cap_over_Cg']==3 and fixed['AND_output_rise_delay_over_R_Cg']==fixed['AND_output_fall_delay_over_R_Cg']==7 and fixed['strictly_below_8_R_Cg'],'Corrected strict delay bound')
    qa=js('pdf_qa.json')
    need(qa['all_final_pages_visually_checked'] and qa['exam_pages']==2 and qa['solution_pages']==6 and qa['overfull_boxes']==0 and qa['typeset_raster_image_count']==0,'PDF QA and editable vectors')
    print('PASS: 2024 midterm; 7 original questions/100 points, 16 MUX +32 CMOS cases, conditional buffer sizing, corrected 7RCg bound, standalone vector PDFs.')
def main():
    import subprocess,sys
    coverage=json.loads((ROOT/'exams'/'COVERAGE.json').read_text(encoding='utf-8-sig'))
    need(len(coverage['completed_exams'])>=1,'Exam coverage count')
    for item in coverage['completed_exams']:
        p=ROOT/'exams'/str(item['year'])/item['exam']
        for key in ['exam_pdf','exam_tex','solution_pdf','solution_tex']:
            artifact=(ROOT/'exams'/item[key]).resolve()
            need(artifact.is_relative_to((ROOT/'exams').resolve()),'Public exam artifact must remain inside exams')
            need(artifact.is_file(),'Public coverage artifact missing')
        for name in ['exam.pdf','solution.pdf']:
            need((p/name).read_bytes().startswith(b'%PDF-'),'Missing exam PDF')
        for name in ['exam.tex','solution.tex']:
            tex=(p/name).read_text(encoding='utf-8')
            need('\\begin{document}' in tex and '\\end{document}' in tex,'Standalone TeX')
            need('\\includegraphics' not in tex and '\\input{' not in tex,'Editable standalone reconstruction')
        if item['status']!='complete':need('missing' in item,'Partial original scope must be labeled')
        for script in sorted(p.glob('verify*.py')):
            subprocess.run([sys.executable,str(script)],cwd=p,check=True)
    verify_2024_midterm()
    p=ROOT/'exams'/'2024'/'final'
    if p.exists():
        s=json.loads((p/'sources.json').read_text(encoding='utf-8'))
        need(sum(s['question_points'])==110,'Preserve original final point total')
        need(s['published_original_exam_pages']==[1,2] and s['local_reviewed_handwritten_answer_pages']==[3,4,5,6,7],'Final source partition')
        q=json.loads((p/'pdf_qa.json').read_text(encoding='utf-8'))
        need(q['all_final_pages_visually_checked'] and q['typeset_raster_image_count']==q['overfull_boxes']==0,'Final PDF QA')
    integrity=private_integrity(coverage)
    if integrity['status']=='not_run':
        print('not_run: private-source integrity; VLSI_PRIVATE_ORIGINALS is not set. All analytical verifiers ran.')
    else:
        print('PASS: private-source integrity;',integrity['original_PDFs_checked'],'PDF SHA-256 checks,',integrity['CSV_image_streams_checked'],'recorded JPEG stream checks.')
    print('PASS:',len(coverage['completed_exams']),'public exam packets; declared scope, editable sources and all analytical evidence.')
    return integrity

if __name__=='__main__':main()
