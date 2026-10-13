# 2024 HW3：4-bit multiplexer-based adder

## 作業要求

依 [homework3.pdf](../assignments/homework3.pdf) Figure 1 完成 4-bit serial-parallel multiplexer-based adder，使用 HSPICE 驗證。上層平行計算各 bit 的 XNOR；carry 沿四個 multiplexer 串接；下層 XNOR 產生 sum。此處的 serial-parallel 是組合邏輯架構，沒有時脈或逐週期串列輸入。

原作業與補充說明規定：CIC018 TT、1.8 V、最小 W = 0.47 μm；採用老師的 testbench 與訊號名稱，CIN = 0；依序輸入 (1,5)、(15,13)、(11,9)、(4,8)、(3,7)、(12,14)、(2,15)、(6,10)，量測平均功率、worst-case delay 與 Σ(WL)。補充評分指標為 area 與 9 ns energy。本解 L = 0.18 μm，所有 MOS 的 W = 0.47 μm。

## 最終設計與來源整合

每位使用 4T upper XNOR、兩個 CMOS inverter、兩組各含兩個 transmission gate 的 sum/carry 網路，共 16T，四位合計 **64T**。令 eᵢ = Xᵢ XNOR Yᵢ，則 Sᵢ = eᵢ XNOR Cᵢ，Cᵢ₊₁ = eᵢ ? Yᵢ : Cᵢ。下層 XNOR 特別以 Cᵢ / complement 作為資料端，eᵢ / complement 作為選擇端；這是弱 upper-XNOR 仍能使外部輸出接近電源軌的關鍵。

先讀取使用者資料夾的 2024 HW3 `VLSI_HW3_111501026_張志華.tar.gz`（88T、W = 0.47 μm、L = 0.24 μm），以及 HW4 `111501026_張志華_HW4.7z` 內的 schematic `four_bit_multbased_adder.sp`（64T）。本解重建相同邏輯、重新撰寫可重現驗證程式、在同一 PWL / model / 量測設定下公平比較。既有報告數值不冒充本次模擬。

另外檢查公開 [NCU_VLSI_Design_2023_HW 的 CLA_cmos.sp](https://github.com/dOwOb1212/NCU_VLSI_Design_2023_HW/blob/main/hw1/CLA_cmos.sp)：雖以 CLA 命名，實際 carry 仍逐位經 mux；該檔為 8-bit，且部分 W = 0.25 / 0.45 μm 小於 2024 下限，測試序列也不同，因此只用於架構交叉比對。

64T upper XNOR 的內部 e 節點可能有 NMOS threshold drop；不可宣稱內部所有節點 full swing。本次要求的 TT / 1.8 V 下，外部五個輸出皆通過指定序列及 512 組電氣驗證。沒有進行跨製程角落、低電壓或負載容限認證。

## 實測結果

HSPICE S-2021.09 win64，TT，25°C，1.8 V，沒有額外輸出電容或 layout 寄生。**兩組量測設定請分清楚：**

| 設定 | 平均 total power | 平均 VDD supply power | 9 ns total energy |
|---|---:|---:|---:|
| 老師原 `.tran 0.1ns 9n`，automatic DELMAX | 69.002216 μW | 37.998479 μW | 621.019943 fJ |
| 精化 `.tran 1p 9n`、`.option delmax=1p` | 69.558498 μW | 37.432840 μW | 626.026482 fJ |

老師指定 `.meas tran pwr avg power` 的 **POWER** 是所有獨立電源對整體電路提供的淨功率，包含輸入 PWL sources；TG 電路也從輸入資料端取得能量，因此它與只算 `-V(vdd) I(vvdd)` 不同。評分 energy 使用 total POWER × 9 ns，沒有以較小的 supply power 代替。

精化結果：指定序列的最大因果 50% 延遲為 **152.910320 ps**，出現在第 8 次切換 (2,15) → (6,10) 的 S0 falling edge；input 50% = 7.950 ns，output 最後 50% crossing = 8.102910320 ns。此為指定輸入序列的 worst-case，沒有宣稱是所有可能輸入轉換的全域 worst-case。

Σ(WL) = 64 × 0.47 × 0.18 = **5.4144 μm²**。這是老師要求的 transistor gate-area proxy，不是實體 layout 面積。

| 候選（同一精化設定） | MOS | Σ(WL) μm² | total energy fJ | delay ps | delay × power fJ |
|---|---:|---:|---:|---:|---:|
| 原 HW3 等價 88T | 88 | 9.9264 | 1005.327 | 247.239 | 27.617 |
| Full-swing 80T，最小尺寸 | 80 | 6.7680 | 824.288 | 137.009 | 12.548 |
| 80T，inverter PMOS 0.94 μm | 80 | 8.1216 | 947.745 | 133.867 | 14.097 |
| 80T，TG W = 0.70 μm | 80 | 8.7552 | 1055.585 | 161.400 | 18.930 |
| **64T，最小尺寸（採用）** | **64** | **5.4144** | **626.026** | **152.910** | **10.636** |
| 64T，PMOS 0.70 μm | 64 | 6.0768 | 676.239 | 149.882 | 11.262 |

六個候選的八組指定向量皆通過。所選 64T 在本次有限候選中兼具最低 area、energy 與 delay × power；80T 雖有較短 delay，其總能量與面積較高。沒有宣稱已找到全域最佳尺寸。

## 驗證與 statistics

八組輸入的 {COUT,S3,S2,S1,S0} 分別為 00110、11100、10100、01100、01010、11010、10001、10000；8 / 8 正確。在每個向量結束後 0.8 ns 採樣，最大低準位 0.00396849 V、最小高準位 1.7910275 V。

額外以真實 HSPICE transistor transient 模擬測試 X、Y = 0…15，CIN = 0 / 1，共 **512 / 512** 組通過。每 case 間隔 2 ns，輸入 ramp 0.1 ns，於 case 起點後 1.8 ns 採樣；外部五輸出皆符合低 ≤ 0.2 V / 高 ≥ 1.6 V，最大低 0.002939216 V，最小高 1.79601867 V。這是全部穩態輸入組合的 transient 採樣檢查，沒有窮舉 512² 個轉換。

延遲採每次對應向量變更、最終方向的最後 0.9 V crossing，避免把短暫 glitch 的第一個 crossing 當作最後穩定結果。指定序列仍有 glitch：總計 12 次額外 50% crossings；所有輸出進入正確 0.2 / 1.6 V band 的最慢 sampled settling bound 是 394 ps（從該次 input 50% 算起）。原始 transient 資料保留為 CSV，使用者不需要 GUI 波形截圖。

## 檔案與重跑

| 檔案 | 用途 |
|---|---|
| `../assignments/homework3.pdf` | 原始題目 |
| `four_bit_multbased_adder.sp` | 最終 64T 電晶體電路；保留老師的 subckt pin order |
| `testbench.sp` | 老師原 PWL 與 `.tran 0.1ns 9n`；只改製程路徑為 `D:/cic018.l` |
| `simulate.py` | 自動產生六個候選、精化功率/延遲與 512 組檢查，並額外執行原 testbench |
| `solution.tex` / `solution.pdf` | 獨立可編譯技術報告 |
| `results/candidates.csv` | 所有候選尺寸、MOS 數、area、total/supply power、energy 與 delay |
| `results/vectors.csv` / `delays.csv` / `settling.csv` | 指定向量輸出電壓、對應 crossing 與 glitch/settling statistics |
| `results/exhaustive_512.csv` | 全 512 組輸入的五個實際電壓與正確性 |
| `results/waveform.csv` | 精化設定的輸出電壓與 VDD 電流，時間解析度 1 ps |
| `results/summary.json` / `instructor_exact.json` | 機器可讀摘要與原始 testbench 設定結果 |

從本資料夾用 PowerShell 執行（需自行持有 HSPICE 與 CIC018 model 的使用授權）：

```powershell
$env:CIC018_MODEL = 'D:\cic018.l'
$env:HSPICE = 'C:\synopsys\Hspice_S-2021.09\WIN64\hspice.com'
python .\simulate.py --work .\.simulation --results .\results
```

`--model`、`--hspice` 可直接指定其他安裝路徑。腳本產生的 model 引用會替換為實際路徑；原 testbench 手動執行時請自行調整 `.lib`。

```powershell
& $env:HSPICE -i .\testbench.sp -o .\.simulation\original
```

執行前先建立 `.simulation` 資料夾。製程 model、學生原稿、raw `.lis` / `.tr0` / license 日誌皆不放公開 repo；公開 statistics 來自本次真實模擬。GitHub 需保留本說明，避免只看到程式卻不知道作業條件與量測定義。
