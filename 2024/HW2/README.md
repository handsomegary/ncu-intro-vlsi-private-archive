# 2024 Homework 2：非理想效應與 pseudo-NMOS NOR

本年度原始 [homework2.pdf](../assignments/homework2.pdf) 是兩道理論題。此目錄包含完整推導 `.tex`、編譯 PDF，以及另外建立並實際執行的 HSPICE 數值驗證。

## 作業要求與解答

1. **Non-ideal Effect（5 分）**：圖中 PMOS 預充電，NMOS 控制電容與 BL 的連接。已知 NMOS 閾值為 `Vt`、接面漏電流為 `IL`，buffer 切換閾值為 `0.4 Vdd`。求 `(a)` 預充電後電容電壓；`(b)` 關閉兩顆電晶體後，儲存資料 1 的保持時間。
   - 題設的固定閾值近似：`VC(0) = Vdd − Vt`。
   - 固定漏電流近似：`tret = C(0.6 Vdd − Vt)/IL`，須有 `Vt < 0.6 Vdd` 才有正的有效保持時間。
   - **讀取拓樸的限制**：原圖 buffer 接 BL，電容在 access NMOS 另一端。SL 關閉後，Out 並不直接監看電容。因此上述是題目預期的「儲存電荷保持時間」，假定後續理想讀取而且 BL 不造成顯著負載。若嚴格要求兩顆電晶體都關閉時，Out 持續可讀，則仍缺少 BL 電容、漏電與讀取流程；解答已說明此限制及重新選取時的 charge sharing。
2. **Logic Gate（5 分）**：圖中上方 PMOS gate 接地，下面兩顆 NMOS 並聯。已知同尺寸下 `Rp = 2 Rn`，且題目刻意把導通電阻視為固定，不區分線性或飽和區。求 `(a)` Boolean function；`(b)` 邏輯低電位限制為 `0.2 Vdd` 時的尺寸。
   - 邏輯為 `Y = NOT(A OR B)`，即 pseudo-NMOS NOR。
   - 原題「smallest voltage of logic 0」按電路意義解讀為**最大允許的 logic-low 電位**。
   - 最壞情況是僅一顆 NMOS 導通；每一顆都須有 `(W/L)n >= 2 (W/L)p`。等通道長度時，每顆 NMOS 寬度至少是 PMOS 的兩倍。
   - 最小對稱比例下，四組輸入 `00/01/10/11` 的 `Vo/Vdd` 分別是 `1、1/5、1/5、1/9`。題目只能決定比例，不能唯一決定絕對 W、L。

## 檔案與執行方式

| 檔案 | 用途 |
|---|---|
| `solution.tex`、`solution.pdf` | 可獨立編譯的完整推導、示意圖、假設、數值表及參考答案比較 |
| `q1_constant_leakage.sp` | 電容與固定電流源抽象模型，驗證保持時間公式；不是原圖完整 MOS 電路 |
| `q2_constant_resistance.sp` | 題設固定電阻模型，驗證四組輸入的分壓 |
| `q2_cic018_tt.sp` | 額外 CIC BSIM3 pseudo-NMOS NOR 驗證，掃描尺寸比例 `1、2、3、4、6、8` |
| `reproduce.py` | 重跑三個 deck，將真實量測表轉成乾淨 CSV；原始 log 保存在本機暫存目錄 |
| `validate_results.py` | 對照理論、檢查 CIC 邏輯電位與對稱性、核對電源電流與功率 |
| `*_measurements.csv` | HSPICE 真實量測，電壓為 V、電流為 A、時間為 s、功率為 W |
| `analytic_expected.csv` | 獨立計算的理論預期，明確標成 `closed_form`，不冒充模擬 |
| `simulation_status.csv`、`validation_summary.json` | 三個 deck 的實際完成狀態與模型條件 |
| `validation_checks.csv` | 43 項檢查的觀測值、預期與容差 |

Windows PowerShell 執行：

```powershell
python .\reproduce.py --hspice 'C:/synopsys/Hspice_S-2021.09/WIN64/hspice.com'
python .\validate_results.py
pdflatex -interaction=nonstopmode -halt-on-error solution.tex
pdflatex -interaction=nonstopmode -halt-on-error solution.tex
```

也可加 `--raw-dir '其他本機資料夾'` 指定原始 log 輸出位置。需使用合法可用的 HSPICE 授權服務；受到網路隔離的執行環境必須允許程式連接既有授權服務。

## 模型與實際驗證結果

使用 PrimeSim HSPICE **S-2021.09 win64**，三個 deck 均以 exit code **0** 完成。驗證日期為 2026-10-13。CIC 製程檔取自本機 `D:/cic018.l`（CIC 0.18 µm、BSIM3、version 1.3、2008-01-21），**不隨公開 repo 散布**；本機必須自行提供。Deck 用 `.protect/.unprotect` 包住模型 include。原始 `.lis`、執行紀錄與授權資訊只留本機。

- **保持時間示例**：自行選用 `Vdd = 1.8 V、Vt = 0.45 V、C = 20 fF、IL = 1 pA`，這些不是題目給定數據。解析結果 `12.600000 ms`，HSPICE 量測 `12.600025 ms`，相對誤差約 `0.000198%`；12.6 ms 時電壓為 `0.72000125 V`。
- **固定電阻驗證**：自行選用 `Rn = 1 kΩ、Rp = 4 kΩ、Vdd = 1.8 V`，量測 `00/01/10/11` 輸出為 `1.8/0.36/0.36/0.20 V`，與解析一致。
- **CIC 驗證**：TT、25 °C、1.8 V，`Lp = Ln = 0.18 µm、Wp = 0.5 µm、Wn = ratio × Wp`。無外加輸出負載，以 `.tran` 先求 DC 工作點並量測穩態值。不是速度或保持時間的製程驗證。

| Wn/Wp | V00 (V) | V01 = V10 (V) | V11 (V) | P01 (mW) |
|---:|---:|---:|---:|---:|
| 1 | 1.800000 | 0.176482 | 0.078389 | 0.242883 |
| 2 | 1.800000 | 0.078122 | 0.036908 | 0.245440 |
| 3 | 1.800000 | 0.049900 | 0.024040 | 0.246127 |
| 4 | 1.800000 | 0.036566 | 0.017786 | 0.246445 |
| 6 | 1.800000 | 0.023779 | 0.011676 | 0.246746 |
| 8 | 1.800000 | 0.017604 | 0.008684 | 0.246891 |

比例 2 時，單一 NMOS 導通的電源電流為 `0.1363557 mA`。比例 1 在這個 TT 模型與偏壓下也符合 `VOL <= 0.36 V`，但 **BSIM3 不採固定電阻，也不強制同尺寸 `Rp = 2 Rn`**，因此不影響作業理論答案的比例至少 2。這不是跨 corner、電壓、溫度的最小尺寸保證。模型物理說明可參考 [UC Berkeley BSIM3v3.2 manual](https://www2.eecs.berkeley.edu/Pubs/TechRpts/1998/ERL-98-51.pdf)。

實際共 **43/43 項**數值檢查通過；保留所有原始有效位數於 CSV，本文表格為方便閱讀而四捨五入。

## 與現成學生答案的整合

先獨立解題，再閱讀本機提供的 `VLSI_HW2.pdf` 手寫答案。其預充電公式、保持時間、NOR 判定、`Rp = 4 Rn` 邊界及尺寸比例 2 皆與獨立推導一致，因此採用這些正確結果。

本版本補上原答案未處理的初始可讀條件、BL 與電容隔離的限制、一般化的尺寸不等式，以及題設固定電阻與真實 BSIM3 模型的差別。原答案 2(a) 開頭寫到 `A=1 AND B=1` 才導通，若當作整個並聯下拉網路的導通條件則不正確，應為任一輸入高就有一條下拉路徑；其後續分情況計算其實採用了正確的 OR 邏輯。未將學生答案或其波形冒充本次模擬結果。
