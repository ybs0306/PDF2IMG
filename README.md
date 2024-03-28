# PDF2IMG

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Poetry](https://img.shields.io/badge/Poetry-%233B82F6.svg?style=for-the-badge&logo=poetry&logoColor=0B3D8D)

把 PDF 轉成照片的工具

## env

需要安裝 [poppler](https://github.com/oschwartz10612/poppler-windows/releases/) 在 local 上，並且路徑加入到環境變數裡

## usage

### windows 上懶人法

把 PDF 拖曳到 exe 上，PDF 旁邊就會生出你 PDF 的照片了

如果你的 PDF 需要密碼才能開，那可以在 `config.ini` 配置檔裡修改**密碼**\
如果想要轉換成其他照片格式，那可以在 `config.ini` 配置檔裡修改**格式**\
如果照片有點模糊/過於清晰，那可以在 `config.ini` 配置檔裡修改 **dpi**

---

如果你想用 Python 來跑，先用 poetry 套件管理處理環境，然後執行

```shell
$ python PDF2IMG.py [YOUR_PDF_FILE_PATH]
```

### 其餘平台

理論上用 Python 執行可以，沒時間試
