# 2024 原始作業與補充說明

原始 PDF 是題目的依據；下表說明各檔案內容與本輪完成範圍。

| 題目 | 原始要求 | 本輪交付 |
| --- | --- | --- |
| [HW1](homework1.pdf) | Static CMOS 邏輯、四輸入四輸出控制電路、pass-transistor 電路分析與 CMOS 實作 | [HW1 解答與驗證](../HW1/)：推導、逐題電晶體圖、truth table |
| [HW2](homework2.pdf) | 非理想 NMOS 傳輸與儲存保持時間；ratioed logic gate 的邏輯與尺寸 | [HW2 解答與驗證](../HW2/)：理論及 HSPICE 輔助驗證；這一年 HW2 的原題本身是理論題 |
| [HW3](homework3.pdf) | 依圖建立四位元 serial-parallel multiplexer-based adder，量測 worst-case delay、power、總電晶體 WL 面積，考量 energy/area | [HW3 設計與統計](../HW3/)：電晶體級 `.sp`、教師原 pattern、自動檢驗與比較 |
| [HW4](homework4.pdf) | HW3 加法器的 layout、擷取網表、pre/post 模擬比較 | [HW4 前佈局 `.sp`](../HW4/)：依使用者指示，交到可模擬 `.sp`；本輪不做 layout、DRC、LVS、PEX 或 post-layout |

## HW3 教師補充條件

- 使用 [原 testbench](hw3_instructor_testbench.sp) 的訊號名稱和 PWL，CIN=0，模擬到 9 ns。
- 依序測試 `(X,Y)=(1,5),(15,13),(11,9),(4,8),(3,7),(12,14),(2,15),(6,10)`。
- 供電 1.8 V，輸出邏輯須對應 0 V/1.8 V，最小 W=0.47 um。
- `energy = average power x 9 ns`；HW3 面積按所有電晶體的 `sum(W_i L_i)` 計算。
- 原始補充說明見 [hw3_clarifications.txt](hw3_clarifications.txt)。本 repo 用統計表與可重現的輸出檢驗呈現結果，依使用者指示不要求 GUI 波形截圖。

## HW4 面積與交付限制

[教師補充說明](hw4_clarifications.txt) 中的 HW4 layout 面積是涵蓋所有材料的長方形面積，**不是** HW3 的 `sum(W_i L_i)`。本輪沒有畫 layout，因此不提供 layout 面積，不把前佈局模擬冒充 post-layout，也不套用既有學生的面積數字。
