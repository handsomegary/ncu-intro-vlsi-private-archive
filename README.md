# Introduction to VLSI Design - 2024

中央大學 EE3032「超大型積體電路導論」，Jin-Fu Li，Fall 2024。

這一輪只處理 **2024 HW1-HW4**。四份原始題目在 [`2024/assignments`](2024/assignments/)。解答以可編譯的 LaTeX、電晶體級 HSPICE 程式及可重現的統計驗證為主。

| 作業 | 交付範圍 |
| --- | --- |
| [HW1](2024/HW1/) | CMOS 邏輯推導、電晶體圖、truth-table 驗證 |
| [HW2](2024/HW2/) | 原始 PDF 的兩道理論題完整推導，另附理想模型與 CIC018 HSPICE 驗證 |
| [HW3](2024/HW3/) | 四位元 XNOR/multiplexer-based adder，原題 9 ns stimuli、面積與能量統計、完整輸入檢驗 |
| [HW4](2024/HW4/) | 沿用通過檢驗的 HW3 設計，交付前佈局 `.sp` 與測試程式；layout、DRC、LVS、PEX、post-layout 結果不在本輪範圍 |

每個作業資料夾的中文 README 都標註原題要求、採用方法、檔案用途、執行方式及驗證結果。

## 本機執行條件

- PrimeSim HSPICE S-2021.09；本次使用安裝在 `C:/synopsys/Hspice_S-2021.09/WIN64/hspice.com` 的版本。
- 使用者提供的 CIC018 製程模型：`D:/cic018.l`，TT corner、1.8 V、25 C。模型由本機讀取，不放入 repo。
- Python 3；個別資料夾內有執行與驗證說明。
- `.tex` 為獨立文件，旁附 PDF 便於直接檢查。圖表和數值由來源程式/量測產生，不依賴 hspui 畫面截圖。

## 來源與比對

先閱讀使用者資料夾內現成解答，再用獨立推導、truth table 和模擬檢查。各題採用與修正的理由見各作業解答及 [SOURCES.md](SOURCES.md)。原始題目保留原檔；既有學生答案、其版圖及 PEX 不冒充這份設計的結果。

## 驗證結果

| 作業 | 已完成的檢驗／量測 |
| --- | --- |
| HW1 | 100 組理想 MOS 開關／邏輯檢查通過，96 列真值資料；這不等於製程模型模擬 |
| HW2 | 三個 HSPICE deck 執行成功，43/43 數值檢查通過；保持時間示例：理論 12.6 ms、實測 12.600025 ms |
| HW3 | 512/512 電晶體級暫態組合通過；六候選選出 64T、`sum(WL)=5.4144 um²` |
| HW4 | 與 HW3 相同網表獨立重跑，8/8 指定向量通過；前佈局結果 |

HW3／HW4 的精化設定（TT、1.8 V、25 C、沒有額外輸出負載、最大時間步 1 ps）：total power **69.558498 uW**、整段 9 ns total energy **626.026482 fJ**。指定序列的最大量測 50% delay 是 **152.910320 ps**；不是所有可能輸入轉換／PVT 的全域最差值。原教師 `.tran 0.1ns 9n` 的量測另列為 **69.002216 uW、621.019943 fJ**，兩種時間步設定不混用。

六候選中 64T 版本的 energy、area、PDP 最低。PDP 是 delay × power；整段 9 ns energy 是 power × 9 ns，兩者不同。採用原因與來源見 [HW3 說明](2024/HW3/README.md)。

## 直接閱讀報告

| 作業 | LaTeX 原稿 | PDF 預覽 |
| --- | --- | --- |
| HW1 | [solutions.tex](2024/HW1/solutions.tex) | [solutions.pdf](2024/HW1/solutions.pdf) |
| HW2 | [solution.tex](2024/HW2/solution.tex) | [solution.pdf](2024/HW2/solution.pdf) |
| HW3 | [solution.tex](2024/HW3/solution.tex) | [solution.pdf](2024/HW3/solution.pdf) |
| HW4 | [solution.tex](2024/HW4/solution.tex) | [solution.pdf](2024/HW4/solution.pdf) |

四份原稿皆已實際編譯並逐頁檢查 PDF；HW1 為繁體中文，以 XeLaTeX 編譯，HW2-HW4 為英文技術報告，可用 PDFLaTeX。各資料夾的 README 全部使用繁體中文。

## 重現與檔案檢查

HSPICE 執行指令與模型覆寫方法見各作業 README。若只要檢查下載的成品、已存量測、來源檔 hash 與連結，可在 repo 根目錄執行：

```powershell
python verify_package.py
```

這個命令只讀取已儲存的實測資料，不冒稱重跑模擬。`MANIFEST.json` 記錄原始 PDF、外部製程指紋與交付檔案 SHA256；文字以 LF 正規化後計算，以免 Windows/Git 換行差異造成誤報。原始模擬與編譯過程檔保留在本機工作區，公開 repo 使用精簡結果。
