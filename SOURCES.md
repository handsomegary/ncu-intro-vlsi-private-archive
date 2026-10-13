# Source review and decisions

檢索/閱讀日期：2026-10-13。以使用者提供的 **Fall 2024** PDF 與教師補充說明為規格；不同年度的程式只能作為架構參考。

## 原題

- `2024/assignments/homework1.pdf` 到 `homework4.pdf`：原始檔逐位元複製，未改寫題目。
- `hw3_instructor_testbench.sp`：保留原始 PWL、輸入/輸出名稱、9 ns 時間與 CIN=0。
- `hw3_clarifications.txt`：最小 W=0.47 um、1.8 V swing、energy=Pavg x 9 ns、使用指定 pattern。
- `hw4_clarifications.txt`：原完整作業需要 layout/DRC/LVS/PEX；本輪依使用者要求交到前佈局 `.sp`，未宣稱完成這些項目。

## 本機既有解答

| 資料 | 已閱讀的內容 | 採用/修正方式 |
| --- | --- | --- |
| HW1 的 `VLSI HW1.pdf` 與第三題更正版 | 所有手寫頁面與電晶體連接，另放大檢查控制反相橫線 | 獨立做布林化簡與連通性驗證、移除可吸收的冗餘支路；重新畫明確的 complementary TG。參考圖中央可辨互補標示，但上支 MOS 符號不清，不斷言原稿接成同極性控制 |
| HW2 的 `VLSI_HW2.pdf` | 儲存電壓、漏電保持時間、pseudo-NMOS NOR 尺寸 | 核心推導交叉核對；補上保持條件、不等式與 BL 讀取限制 |
| HW3 的學生 `.tar.gz` | 報告及 88T 的 XNOR/TG/mux 程式 | 以相同測試條件重跑，與獨立整理的設計比較；量測結果見 HW3 |
| HW4 的學生 `.7z` | 3 頁 PDF、64T 前佈局程式、實際 PEX 檔與測試程式 | 參考 XNOR/mux 架構和交付方式；報告將 pre/post 名稱寫反，且測試程式同時放置兩個 DUT，總 `power` 不能直接當單一設計數值。其 layout 面積與 PEX 不屬於本輪設計，不沿用其數字 |

## 公開搜尋

已搜尋 `Jin-Fu Li 2024 homework VLSI github`、`EE3032 Homework github`、`NCU VLSI 2024`、`four_bit_multbased_adder`、`NCU VLSI` 等查詢。搜尋可見性有限；沒有據此宣稱網路上不存在其他 2024 解答。

- [dOwOb1212/NCU_VLSI_Design_2023_HW](https://github.com/dOwOb1212/NCU_VLSI_Design_2023_HW)：已讀取 [`hw1/CLA_cmos.sp`](https://github.com/dOwOb1212/NCU_VLSI_Design_2023_HW/blob/main/hw1/CLA_cmos.sp)，Git blob SHA `9bee2ead3081e2abb2e5e19fee6f47c9414c267c`。其 unit 也使用兩個 XNOR 和 carry mux，可核對 carry 方程；實際為逐位 carry 傳遞，檔名中的 CLA 不等於 lookahead。此檔是 **8-bit**，W=0.25/0.45 um、不同測試向量，不符合 2024 W>=0.47 um 的規格。未把整個程式直接放入本 repo。
- [Yeimaoz/NCU_VLSI](https://github.com/Yeimaoz/NCU_VLSI)：GitHub 搜尋有命中，但 API 回應 `409 Git Repository is empty`，沒有可讀的解答可採用。

每份新解答保留獨立推導、出處與檢驗條件。既有答案中沒有驗證過的數值不當作本次量測。

## HSPICE 量測定義

已核對安裝版本隨附的官方 PrimeSim HSPICE 文件 `docs_help/hspice_6/selecting_simulation_output_parameters.htm`，章節 **Power Output**。`POWER` 計入耗散與儲能變化，按符號慣例等於所有獨立來源吸收功率之負和，因此也包含 PWL 輸入的能量；不等於只算 VDD 的供電功率。本 repo 分列 total POWER 與 VDD-only power，並以教師指定的 total POWER 計算 9 ns energy。
