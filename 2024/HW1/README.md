# 2024 HW1：靜態 CMOS 與資料選擇電路

本資料夾是 EE3032 Introduction to VLSI Design（李進福，Fall 2024）HW1 的完整推導解答。這份作業是手寫／推導題；本解答使用 LaTeX 整理，附電晶體圖、真值表及可重現的理想開關連通性驗證。

## 作業要求與解答概要

| 題號 | 題目要求 | 採用的解法 |
| --- | --- | --- |
| 1(a) | 用 static CMOS 實現 `f = NOT(x + y + wyz)`；只提供正相輸入，須畫電晶體圖。 | 由吸收律 `y + wyz = y`，得到二輸入 NOR。pMOS 串聯、nMOS 並聯，共 4T；`w`、`z` 不影響輸出。 |
| 1(b) | 用 static CMOS 實現 `f = x'y' + x'z' + y'z'`；只提供正相輸入。 | `f = NOT[xy + z(x+y)]`。PDN/PUN 各 5T，共 10T，無須輸入反相器。 |
| 2 | 4 個資料輸入、4 個控制輸入、4 個輸出，實現原題表格的四種循環選擇。 | 16 個 CMOS transmission gate，加上 4 個共用控制反相器，共 40T。完整接線圖逐一標示資料來源及 `c_j`／`c_j'`。原題控制是 one-hot。 |
| 3(a) | 分析原圖 pass-transistor 電路的邏輯函數。 | `F = AB + A'B'`，即 XNOR。 |
| 3(b) | 用 CMOS 實現同樣函數。 | 主要解答為 8T static CMOS 核心；若沒有互補輸入，加 2 個 inverter，共 12T。另附完整互補控制的 8T TG 版本（包含輸入反相器）。 |

`'` 表示反相，`+` 表示 OR，相乘表示 AND。第 1(a) 題原始 PDF 的長橫線涵蓋整個 `x + y + wyz`，不能遺漏。

題 2 的四列以 `(z3,z2,z1,z0)` 表示：

| 有效控制 | 輸出 |
| --- | --- |
| `c3=1` | `(a3,a2,a1,a0)` |
| `c2=1` | `(a2,a1,a0,a3)` |
| `c1=1` | `(a1,a0,a3,a2)` |
| `c0=1` | `(a0,a3,a2,a1)` |

其餘控制均為 0。原題沒有指定非 one-hot 控制；TG 結構在全部為 0 時浮接、同時選擇多個資料時可能短接資料。正文另說明若要求所有控制碼都有定義，可改用完整 static CMOS AND-OR 網路。

## 檔案用途

| 檔案 | 用途 |
| --- | --- |
| [solutions.tex](solutions.tex) | 可獨立編譯的繁體中文解答。內含 TikZ 電晶體圖，不依賴外部圖片。 |
| [solutions.pdf](solutions.pdf) | 供直接閱讀與檢視品質的編譯版本。 |
| [verify_logic.py](verify_logic.py) | 僅使用 Python 標準函式庫的逐輸入驗證，依實際 MOS 端點建立導通圖。 |
| [truth_tables.csv](truth_tables.csv) | 96 列主電路逐輸入結果，包含預期值、實際值與 PASS。 |
| [verification.json](verification.json) | 完整測試計數、電晶體數及解答原稿 SHA-256。 |

原題另存於 repository 的 [2024/assignments/homework1.pdf](../assignments/homework1.pdf)。兩份原有手寫參考答案由使用者本機提供，來源與差異詳列於解答最後一頁；未將其內容偽裝成新作的原創，也未因作者／授權未標示而額外公開手寫檔案。

## 驗證方式與結果

在此資料夾執行：

```powershell
python .\verify_logic.py
```

結果：**PASS，100 組案例**。

| 測試 | 案例數 |
| --- | ---: |
| 1(a)：全部 `w,x,y,z`，含原式與化簡式一致、PUN/PDN 互補及無浮接／電源直通 | 16 |
| 1(b)：全部 `x,y,z`，含 SOP/POS/因式分解式與 10T 導通圖 | 8 |
| 2：四種 one-hot 選擇乘以 16 組資料，檢查展開 MOS 後的完整資料連通性 | 64 |
| 3：static CMOS 的全部 `A,B` | 4 |
| 3：修正 TG 版本的全部 `A,B` | 4 |
| 共用反相器的 0／1 | 2 |
| 題 2 非規格控制示例：零選擇浮接、多選擇資料相接 | 2 |

這是理想二進位 MOS 開關驗證，沒有使用 HSPICE，也不宣稱驗證製程、電晶體尺寸、延遲、類比電壓擺幅或切換暫態。本作業 HW1 未要求這些模擬；圖中的 body 接法及原 NMOS-only 電路的高電位損失另有說明。

## 參考答案比對與修正

已逐頁閱讀原題 1 頁、`VLSI HW1 第三題(2)電路畫錯.pdf` 4 頁（含封面）與 `VLSI HW1.pdf` 3 頁。

- **1(a)：** 兩份參考的 10T 結構保留了可吸收的 `wyz` 支路。本解答採更精簡、只用正相輸入的 4T NOR。第一份參考把冗餘支路標成 `z'`，不合正相輸入條件；由於支路冗餘，這個標示不影響其輸出真值。
- **1(b)：** 兩份參考的 12T minority 結構有效。本解答獨立因式分解，改成 10T，並檢查所有真值及電源連通性。
- **2：** 參考的循環資料接線有效，保留這種 TG 架構，補齊共享反相控制、40T 計數及 one-hot 假設。
- **3：** 兩份參考均正確辨識 XNOR。放大第一份參考可辨認互補控制的橫線；上支 MOS 類型的符號不清，不能據此斷言是同極性控制或接線錯誤。本解答重新畫出明確標示 nMOS／pMOS gate 的完整 TG 替代版。第二份的 static CMOS 結構有效，與本解答獨立推導一致。

## 編譯

```powershell
xelatex -interaction=nonstopmode -halt-on-error .\solutions.tex
```

需要 XeLaTeX、`xeCJK`、`fontspec`、`tikz` 與標準 LaTeX 數學套件。字型依序偵測 Windows 的 Times New Roman／Microsoft JhengHei，或使用 Latin Modern Roman／Noto Serif CJK TC／FandolSong-Regular 備援。已通過 Codex 內建 LaTeX 編譯器，並另導出 PDF 逐頁目視檢查。
