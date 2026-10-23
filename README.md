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

## 直式課室佈局

1. **講授區** — 白板、講桌
2. **電腦區** — 2×3 電腦桌
3. **討論區** — 地毯＋小組座位
4. **儲物區** — 書架、櫃、影印機

## 觸控（手機優先）

| 操作 | 功能 |
|---|---|
| 「開始上課」 | 進入課室 |
| 左下虛擬 D-pad | 移動老師 |
| 右下「互動／關閉」 | 開／關區域資訊 |
| 點擊區域 | 顯示資訊卡 |
| WASD／方向鍵 | 移動 |
| 1–4／E／Esc | 區域、互動、關閉 |

## 角色與移動

- **角色臉與衣著**來自 CC0 Pixel Office 圖集（非程序醜臉）
- **四向面向** + walk／idle；步行幀與位移同步
- **AABB 碰撞**：腳底盒 vs 傢俬底座；X／Y 分離
- **鏡頭**：360×640 軟跟隨老師

## 素材來源與授權（全部可商用／可再分發）

詳見 [`assets/CREDITS.md`](assets/CREDITS.md)。摘要：

| 素材 | 作者 | 授權 | 用途 |
|---|---|---|---|
| [Pixel Office Asset Pack](https://2dpig.itch.io/pixel-office) | 2dPig | **CC0** | 傢俬、電腦、角色臉、貓狗 |
| [Roguelike Indoor Pack](https://opengameart.org/content/roguelike-indoor-pack) | Kenney | **CC0** | 補充室內傢俬／植物 |
| [indoor office appliances](https://opengameart.org/content/indoor-office-appliances) | semtex99 | **CC0** | 顯示器、櫃、書架道具 |
| [16x16 base sprites](https://opengameart.org/content/16x16-base-sprites) | Unnamed (OGA) | **CC0** | （舊方案參考；現行步行以 Pixel Office 全身＋腿位移為主） |

授權檔副本：`assets/vendor-licenses/`。原始下載暫存：`vendor/src/`（可選，不影響執行）。

## 技術

- 靜態 SPA：`index.html` + `assets/`
- 適合 GitHub Pages 根目錄部署
- 繁體中文 UI；離線可玩

## 限制

- 非完整課程系統，僅氣氛／導覽場景
- 無存檔、無音效、無多人
