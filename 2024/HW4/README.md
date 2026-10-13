# 2024 HW4：做到可模擬的 `.sp`

## 原題與本輪範圍

[原始 homework4.pdf](../assignments/homework4.pdf) 要求將 HW3 的四位元加法器畫 layout、擷取網表、比較 pre/post-layout。依使用者指定，本輪交付 **前佈局電晶體級 `.sp`、可執行 testbench、真實統計與說明 `.tex`**。

Layout、DRC、LVS、PEX、post-layout 模擬及 physical layout area 不在本輪範圍，沒有宣稱完成。原課程的完整繳交規格見 [教師補充說明](../assignments/hw4_clarifications.txt)。

## 檔案用途

| 檔案 | 用途 |
| --- | --- |
| [four_bit_multbased_adder.sp](four_bit_multbased_adder.sp) | HW3 最終 64T 網表逐位元複製，元件、尺寸與 pin order 相同 |
| [testbench.sp](testbench.sp) | 單一 DUT、原教師九個輸入 source、TT/1.8 V/25 C、9 ns；加入 1 ps 最大時間步與輸出量測 |
| [reproduce.py](reproduce.py) | 呼叫本機 HSPICE，檢查八組指定向量與能量一致性；可更換模型和執行檔路徑 |
| [vectors.csv](vectors.csv) | 每組輸入、預期整數和、五個實際輸出電壓、檢驗結果 |
| [statistics.json](statistics.json) | 實測 power/energy、條件、case count、網表與模型 SHA256 |
| [solution.tex](solution.tex) / [solution.pdf](solution.pdf) | 可編譯報告與預覽，含 carry/sum 方程、既有答案審查與本輪限制 |

## 設計與量測結果

每位元使用 `e = X XNOR Y`、`S = e XNOR CIN`、`COUT = e ? Y : CIN`，串接四個 cell。上層 4T XNOR 的內部 `e` 可能有 threshold drop；下層 TG-XNOR 用 CIN/CINbar 當 data，並以 e/ebar 作 select。輸出電位以實際電晶體模擬確認，沒有假設內部節點都是理想 1.8 V。

此資料夾已獨立執行：

| 條件／數值 | 結果 |
| --- | --- |
| Process / simulator | 使用者本機 CIC018 TT / HSPICE S-2021.09 |
| 供電／溫度／時間 | 1.8 V / 25 C / 0-9 ns |
| 額外輸出負載 | 無；不代表任意負載下有相同性能 |
| 最大時間步 | 1 ps |
| 電晶體數／每顆 W、L | 64 / 0.47 um、0.18 um |
| Schematic `sum(WL)` | 5.4144 um²；不是 physical layout area |
| HSPICE total average power | 69.558498 uW |
| VDD supply average power | 37.4328403 uW，和 total power 分開報告 |
| Total energy | 626.026482 fJ = 0.626026482 pJ／整段 9 ns |
| 指定八組向量 | 8/8 全通過，能量 `Pavg x 9ns` 一致 |

輸入依序為 `(1,5),(15,13),(11,9),(4,8),(3,7),(12,14),(2,15),(6,10)`，CIN=0；在 1.8、2.8、…、8.8 ns 取樣。各 bit 的預期 0 使用 -0.02~0.2 V，預期 1 使用 1.6~1.82 V 驗證，所有實際電位見 CSV。這些容許範圍不是對未測 PVT 或負載的保證。

[HW3](../HW3/) 另有同一網表的 512/512 電晶體級暫態檢驗、指定序列的最大量測延遲、六個候選比較，以及原始 0.1 ns-output-step testbench 的量測。不能把不同時間步的結果混成同一組數據。

## 執行方式

在本資料夾執行（Python 只使用標準函式庫）：

```powershell
python reproduce.py --model "D:/cic018.l" --hspice "C:/synopsys/Hspice_S-2021.09/WIN64/hspice.com"
```

也可設定環境變數 `CIC018_MODEL`、`HSPICE`。模型由本機讀取，不提交到 GitHub。原始模擬紀錄存在 `run_artifacts/`，CSV/JSON 是可公開檢查的精簡結果。若 HSPICE 無法取得授權或模型不存在，程式會失敗，不會把未執行的結果標成成功。

## 既有答案比較

已讀使用者提供的 `111501026_張志華_HW4.7z` 中三頁報告、前佈局 `.sp`、測試程式與 PEX。取其 4T XNOR/TG/mux 架構作為候選，再獨立整理介面、共享反相信號及在相同條件下驗證。六候選中選用的 64T min 版本在 energy、area、PDP 都較好，詳見 HW3；沒有宣稱全域最佳。

既有報告把 pre/post 標籤寫反，且原 testbench 同時放前、後佈局兩個 DUT，直接 `avg power` 會合併功耗。本輪只放單一 DUT；不沿用他人的 layout 面積、PEX 或報告能量數字。舊電路另通過 512 組 DC 輸入檢查；新網表的 512 組 transient 檢查是另一份驗證，兩者不混稱。
