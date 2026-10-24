# 像素課室（Pixel Classroom）

香港中學 ICT 電腦室像素場景 — 給老師 **Lap Cheung Tsao** 的 cozy 課室模擬。

**口號：** 上課，像玩遊戲一樣

## 開啟

直接用瀏覽器開啟 `index.html`（需與 `assets/` 同目錄；離線、無 CDN）。

GitHub Pages：https://tlc-cmyk.github.io/pixel-classroom/

（若見舊畫面，請強制刷新：Ctrl/Cmd+Shift+R，或手機清除網站資料）

## 畫布（直式手機全螢幕）

- 邏輯解析度：**360 × 640**（約 9:16 portrait）
- CSS：`100vw` × `100dvh`／`100svh`，含 `safe-area-inset`
- 桌面寬螢幕：居中直式機框預覽
- 圖集：`assets/atlas.png` + `assets/atlas.json`（本地載入，無 CDN）
- **書枱／角色**：課桌約 72×56（Pixel Office 組合 CRT 枱）、學生高 44、老師高 54；校服來自 IT 海報（男白恤衫西褲／女白恤衫格裙領帶）

## 課室佈局（4×4）

1. **講台** — 白板、講桌、窗戶／門；玩家扮演老師
2. **課室座位** — **4×4 = 16 張學生枱**，中央走道；每枱有椅、檯、螢幕
3. **16 位同學** — 全部坐下；**男／女校服交替**（海報造型像素化），各有中文姓名
4. **後排** — 書架、沙發、影印機、貓

## 點名／互動

走近同學（約一格距離）會出現「E 點名」提示：

| 操作 | 功能 |
|---|---|
| E／F 或右下「點名」 | 開該位同學面板 |
| 點學生／書枱 | 老師夠近時開點名面板 |
| 出席／缺席 | 切換該生出席狀態（頂欄顯示出席人數） |
| 打招呼 | 同學冒出對話泡泡＋舉手回應 |
| Esc／關閉 | 關面板 |

## 微動畫

- 坐下同學：**idle bob**（輕微上下晃）
- **偶發舉手**（側身幀＋金色小旗）
- **眨眼**（眼帶短線 overlay；圖集無獨立 blink 幀時的近似）

## 音效（Web Audio，無 CDN）

| 事件 | 聲效 |
|---|---|
| 步行 | 可選柔和低音（節流） |
| 點名／互動 | 雙音 beep |
| 面板開／關 | 升／降 chirp |
| 出席切換、打招呼 | 短促音階 |

首次操作會 resume AudioContext（瀏覽器自動播放政策）。

## 觸控（手機優先）

| 操作 | 功能 |
|---|---|
| 「開始上課」 | 進入課室 |
| 左下虛擬 D-pad | 移動老師 |
| 右下「點名／關閉」 | 開／關互動面板 |
| WASD／方向鍵 | 移動 |
| 1–2 | 區域資訊 |

## 角色與移動

- **角色骨架**來自 CC0 Pixel Office；**校服**按學校 IT 支援海報重繪（白恤衫、校徽、男西褲／女格裙領帶）
- **四向面向** + walk／idle；步行幀與位移同步
- **AABB 碰撞**：腳底盒 vs 書枱／講桌底座；X／Y 分離
- **鏡頭**：360×640 軟跟隨老師

## 素材來源與授權（全部可商用／可再分發）

詳見 [`assets/CREDITS.md`](assets/CREDITS.md)。摘要：

| 素材 | 作者 | 授權 | 用途 |
|---|---|---|---|
| [Pixel Office Asset Pack](https://2dpig.itch.io/pixel-office) | 2dPig | **CC0** | 傢俬、電腦、角色臉、貓狗 |
| [Roguelike Indoor Pack](https://opengameart.org/content/roguelike-indoor-pack) | Kenney | **CC0** | 補充室內傢俬／植物 |
| [indoor office appliances](https://opengameart.org/content/indoor-office-appliances) | semtex99 | **CC0** | 顯示器、櫃、書架道具 |

授權檔副本：`assets/vendor-licenses/`。原始下載暫存：`vendor/src/`（可選，不影響執行）。

## 技術

- 靜態 SPA：`index.html` + `assets/`
- 適合 GitHub Pages 根目錄部署（`main`）
- 繁體中文 UI；離線可玩；音效用 Web Audio oscillators

## 限制

- 非完整課程系統，僅氣氛／導覽／點名場景
- 無雲端存檔、無多人；出席狀態僅本機當次
