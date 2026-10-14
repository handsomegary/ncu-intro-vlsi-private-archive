"""Saved-evidence checks for the authentic original-prompt 2013–2019 extension.

No simulator or compiler is launched; report coverage, numeric measurements and
declared sizing conditions are checked from published data. Set
VLSI_PRIVATE_ORIGINALS to verify frozen hashes of private original prompts;
without it, original integrity is explicitly not_run.
"""
from pathlib import Path
import csv,hashlib,json,math,os
ROOT=Path(__file__).resolve().parent/'homework'
ACTIVE={2013:[1,2,3],2015:[1,2,3,4],2016:[3],2017:[1,2,3,4],2018:[1,2],2019:[2]}
# Fingerprints recorded before originals were removed from the public tree.
ORIGINAL_SHA256={
    '2013/assignments/homework1.pdf':'f10c5c107f247cd233de54855e0bc76f024301480bba97a1a4588094be80baac',
    '2013/assignments/homework2.pdf':'9cf70011bf1523685cfa989b216da691d817a3c6dd9621c53e98d01644fe30fc',
    '2013/assignments/homework3.pdf':'2c1b3d1be71fda40ecd3ffb830fa35707c2bb3f0028b71b8019ca15149163a82',
    '2015/assignments/homework1.pdf':'5f12fd2ce7f66b02adf4eb6aa2897c3bb1b9843c1359583ffe166ce6c5431f63',
    '2015/assignments/homework2.pdf':'50486dbce58ff01494e7e325ce140cf57545458d5416eb15aef1587b7cefb2cd',
    '2015/assignments/homework3.pdf':'2e839750e3f5c44dab208db4689b14cee99f8d9203064d53372c5c3459203ece',
    '2015/assignments/homework4.pdf':'cb83588d255dc52cf7d226f16bdc2436ac570e907fcb9b8f211376b5daed4f72',
    '2016/assignments/homework3.pdf':'6be83e172ba28cfe3bce6b97bcd101afd9c2480ba90714c27d70080bcdb2004a',
    '2017/assignments/homework1.pdf':'9d6dec85a4fd1a9de6c045c8447e61ce88d09a270cc89c39612a9b042b8b29be',
    '2017/assignments/homework2.pdf':'9cd5d02fda2b755a2f501d47867c29bd7f63a8a2527ebfdd7527b105d4cffe6e',
    '2017/assignments/homework3.pdf':'04d3cd0cdee1fc2a0ca0488e16a0ff9b8154c67587d9fc734b5967adeaed1602',
    '2017/assignments/homework4.pdf':'a8fe77fbc1c73087b71667d66801ab89703356e6b140d13a5dfd707ad432b84c',
    '2018/assignments/homework1.pdf':'a3b82c6a88e072396c8270edc137c507a3f53141cd92bb2aebc97fa8f29b6654',
    '2018/assignments/homework2.pdf':'f070cd4e3876fc5cf558f4afb8cc92237169745ca30081cff12c6a593d412c87',
    '2019/assignments/homework2.pdf':'fba75f1a9985fd6bf7a9ec7a28015be7805625701f14fb49b1bc6bb1ea5dcfa6',
}
def need(ok,msg):
    if not ok:raise AssertionError(msg)
def js(rel):return json.loads((ROOT/rel).read_text(encoding='utf-8-sig'))
def rows(rel):
    with (ROOT/rel).open(encoding='utf-8-sig',newline='') as f:return list(csv.DictReader(f))
def near(a,b,rtol=1e-6):return math.isclose(float(a),float(b),rel_tol=rtol,abs_tol=1e-12)
def adder_bit(bits,node):
    total=sum(map(int,bits))
    return total%2 if node.lower()=='s' else (1-int(total>=2) if node.lower()=='nco' else int(total>=2))
def level(bit,value):
    v=float(value)
    return math.isfinite(v) and (-.02<=v<=.2 if bit==0 else 1.6<=v<=1.82)
def private_original_integrity():
    configured=os.environ.get('VLSI_PRIVATE_ORIGINALS')
    if not configured:
        print('Private original integrity: not_run (VLSI_PRIVATE_ORIGINALS not set; 15 known hashes not checked).')
        return {'status':'not_run','checked':0,'expected':len(ORIGINAL_SHA256)}
    private=Path(configured).expanduser()/'homework'
    for relative,expected in ORIGINAL_SHA256.items():
        path=private/relative
        need(path.is_file(),f'Private original missing: homework/{relative}')
        data=path.read_bytes()
        need(data.startswith(b'%PDF-'),f'Private original is not a PDF: homework/{relative}')
        need(hashlib.sha256(data).hexdigest()==expected,f'Private original SHA256 mismatch: homework/{relative}')
    print('Private original integrity: PASS (15 exact SHA256 matches).')
    return {'status':'PASS','checked':len(ORIGINAL_SHA256),'expected':len(ORIGINAL_SHA256)}
def main():
    private_original_integrity()
    catalog=js('COVERAGE.json')
    need(catalog['completed_assignments']==31 and catalog['newly_added_older_assignments']==15,'Coverage counts')
    for y,hwlist in ACTIVE.items():
        year=ROOT/str(y)
        need((year/'SOURCES.md').is_file(),'Source review missing')
        for h in range(1,5):
            folder=year/f'HW{h}'
            if h in hwlist:
                need((folder/'solution.tex').is_file() and (folder/'solution.pdf').read_bytes().startswith(b'%PDF-'),f'{y} HW{h} reports')
                need((folder/'README.md').is_file(),f'{y} HW{h} reproduction README')
            else:need(not (folder/'solution.tex').exists(),f'Unrequested student-only task {y}/HW{h}')
        for p in year.rglob('*'):
            need(not p.is_file() or p.suffix.lower() not in {'.l','.lic','.gds','.pex','.docx','.zip','.7z'},f'Private/out-of-scope artifact {p}')
            if p.is_file() and p.suffix=='.csv':
                for r in rows(p.relative_to(ROOT).as_posix()):
                    for k in ['passed','pass','pass_','pass_level','all_logic_pass','logic_pass','pass_logic_levels']:
                        if k in r:need(r[k].lower() in ['true','1'],f'Failed saved check {p}: {r}')
    for y in [2012,2014]:
        p=ROOT/str(y)
        need(not any(p.rglob('solution.tex')) if p.exists() else True,f'Student-only year {y} should be skipped')
    need(js('2013/HW1/verification.json')['status']=='PASS','2013 HW1')
    v=js('2013/HW1/verification.json');need(v['truth_table_cases']==32 and v['unequal_length_current_points']==80800,'2013 proof counts')
    v=js('2013/HW2/verification.json');need(v['status']=='PASS' and near(v['critical_delay_ns'],.6),'2013 clock calculation')
    v=js('2013/HW3/results/summary.json')
    need(v['status']=='PASS' and v['TG_dimensions_um']=={'WN':10,'WP':20,'L':.18} and v['mux_output_load_fF']==10,'2013 prescribed geometry/load')
    need(v['logic_cases']==2048 and v['mux_electrical_transition_cases']==16,'2013 logic/electrical coverage distinction')
    ds=rows('2013/HW3/results/mux_delays.csv');need(len(ds)==16,'2013 mux rows')
    need(all(float(r['tree_delay_ps'])<float(r['baseline_delay_ps']) for r in ds),'2013 same-condition improvement')
    for which in ['baseline','tree']:
        need(near(max(float(r[which+'_delay_ps']) for r in ds),v[which+'_worst_delay_ps']),'2013 maximum from saved rows')
    power=rows('2013/HW3/results/inverter_power.csv');need(len(power)==5,'2013 inverter curve')
    for r,load in zip(power,[.1,.3,.5,.7,1]):
        need(near(r['CL_pF'],load),'2013 prescribed power loads')
        need(near(r['E_sc_overlap_fJ'],float(r['Psc_overlap_uW'])*v['inverter_period_ns']),'2013 power/energy units')
        need(near(r['external_load_switching_power_uW'],load*v['VDD_V']**2/v['inverter_period_ns']*1000),'2013 external load power')
        need(float(r['high_V'])>=1.6 and float(r['low_V'])<=.2,'2013 settled power levels')
    need('LX4' in v['Psc_method'],'2013 intrinsic channel-current definition')
    need(js('2015/HW1/verification.json')['all_pass'] and js('2015/HW2/verification.json')['all_pass'],'2015 theory checks')
    v=js('2015/HW3/verification.json');need(v['all_levels_pass'] and v['max_AND_timestep_difference_ps']<.2,'2015 AND/convergence')
    need(v['power_loads_pF']==[.1,.3,.5,.7,1],'2015 prescribed power loads')
    need('LX4' in v['Psc_definition'],'2015 intrinsic channel-current definition')
    ps=rows('2015/HW3/power_vs_load.csv');need(len(ps)==5,'2015 power curve')
    for r,load in zip(ps,[.1,.3,.5,.7,1]):
        need(near(r['load_pF'],load),'2015 saved power loads')
        need(math.isclose(float(r['overlap_cycle_energy_J']),float(r['Psc_overlap_W'])*v['period_power_ns']*1e-9,rel_tol=1e-8,abs_tol=1e-20),'2015 power/energy units')
        need(near(r['Psw_external_W'],load*1e-12*v['VDD_V']**2/(v['period_power_ns']*1e-9)),'2015 external load power')
        need(float(r['settled_high_V'])>=1.6 and float(r['settled_low_V'])<=.2,'2015 settled power levels')
        need(abs(float(r['trace_integration_power_W'])-float(r['Psc_overlap_W']))<3e-13,'2015 independent trace integration')
    need(all(float(a['Psc_overlap_W'])>float(b['Psc_overlap_W'])>0 for a,b in zip(ps,ps[1:])),'2015 measured power trend')
    v=js('2015/HW4/verification.json')
    for design in ['mirror','domino']:
        need(v[design]['all_logic_pass'],'2015 FA levels')
        for metric in v[design]['fine_step_balance'].values():need(metric['relative_difference']<.03,'2015 slew balance')
        need(v[design]['max_delay_timestep_difference_ps']<.3,'2015 FA convergence')
    need(v['mirror']['device_count']==28 and v['domino']['device_count']==38,'2015 circuit counts')
    for design in ['mirror','domino']:
        data=(ROOT/'2015'/'HW4'/(design+'.sp')).read_bytes().replace(b'\r\n',b'\n')
        need(hashlib.sha256(data).hexdigest()==v[design]['netlist_SHA256_UTF8_LF'],'2015 verified netlist provenance')
        logic=rows('2015/HW4/'+design+'_logic.csv')
        need(len(logic)==(112 if design=='mirror' else 24),'2015 measured logic coverage')
        for r in logic:
            expected=adder_bit(r['inputs_after'] if design=='mirror' else r['input_bits'],r['node'])
            need(int(r['expected'])==expected and level(expected,r['voltage_V'] if design=='mirror' else r['evaluate_V']),'2015 independent sum/carry and voltage check')
            if design=='domino':need(level(0,r['reset_V']),'2015 domino precharge output')
    for y in ['2016','2017']:
        v=js(y+'/HW3/results/and_gate/summary.json')
        need(v['all_logic_levels_pass'] and len(v['cases'])==3,'Equal-size AND cases')
        ds=rows(y+'/HW3/results/and_gate/delays.csv');need(len(ds)==36 and all(float(r['delay_ps'])>0 for r in ds),'AND delays')
        p=js(y+'/HW3/results/power/summary.json');need(len(p['rows'])==5 and p['input_rise_fall_ns']==3,'Power input/curve')
        values=[r['Psc_uW'] for r in p['rows']]
        need(all(a>b>0 for a,b in zip(values,values[1:])),'Recorded Psc trend')
        for r in p['rows']:
            need(near(r['Eshort_fJ'],r['Psc_uW']*p['period_ns']),'Psc energy units')
            need(near(r['Pload_switching_uW'],r['CL_pF']*1e-12*p['VDD_V']**2/(p['period_ns']*1e-9)*1e6),'External load switching power')
            need(r['Vhigh']>=1.6 and r['Vlow']<=.2,'Settled power levels')
    need(js('2017/HW1/verification.json')['all_pass'],'2017 logic')
    v=js('2017/HW4/results/summary.json');need(v['mirror_directed_transitions']==56 and v['domino_input_states']==8,'2017 FA coverage')
    for design in ['mirror','domino']:
        d=v['designs'][design];need(d['all_logic_pass'] and d['balanced'],'2017 FA status')
        for metric in d['statistics'].values():need(metric['imbalance_percent']<=1.01,'2017 slew balance')
        logic=rows('2017/HW4/results/'+design+'_logic.csv')
        need(len(logic)==(112 if design=='mirror' else 32),'2017 measured logic coverage')
        for r in logic:
            expected=0 if r['old']=='precharge' else adder_bit(r['new'],r['node'])
            need(int(r['expected'])==expected and level(expected,r['voltage_V']),'2017 independent sum/carry and voltage check')
    need(js('2018/HW1/verification.json')['boolean_cases']==40,'2018 logic counts')
    need(js('2018/HW1/verification.json')['square_law_points']==5050,'2018 square law')
    for y in ['2018','2019']:
        v=js(y+'/HW2/validation.json');need(v['status']=='PASS' and v['rc_fanins']==8 and v['slew_cases']==2,'HW2 simulations')
        need(v['fast_input_output_fall_ps']<v['slow_input_output_fall_ps'],'Input slew ordering')
        rs=rows(y+'/HW2/rc_checks.csv');need(len(rs)==8,'RC fanin count')
        for r in rs:
            n=int(r['fanin']);need(near(r['expected_rise_ps'],2*n*n) and near(r['expected_fall_ps'],n+1),'Independent RC formula')
            need(near(r['measured_rise_first_moment_ps'],2*n*n,.002) and near(r['measured_fall_first_moment_ps'],n+1,.002),'Measured RC first moments')
        need(near(v['node_x_Cg_ratio'],8/3),'Gate capacitance ratio')
    print('PASS: 15 older assignments; reports, geometry, published numeric evidence, power units, sizing and source omissions. Private original integrity is reported separately above.')
if __name__=='__main__':main()
