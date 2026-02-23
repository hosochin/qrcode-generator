# QRコードSVG生成CLIツール

印刷用途に適したSVGフォーマットのQRコードをコマンドラインから生成するツールです。

## セットアップ

```bash
pip install -r requirements.txt
```

## 使い方

```bash
python qrgen.py <データ> [オプション]
```

### 基本例

```bash
# URLをQRコード化（output.svg を生成）
python qrgen.py "https://example.com"

# 出力ファイル名を指定
python qrgen.py "https://example.com" -o myqr.svg

# テキストをQRコード化
python qrgen.py "Hello World" -o text.svg
```

## オプション

| オプション | デフォルト | 説明 |
|---|---|---|
| `data` | 必須 | QRコードに埋め込むデータ（URLやテキスト） |
| `-o, --output` | `output.svg` | 出力ファイルパス |
| `--scale` | `10` | スケール（大きいほど高解像度） |
| `--error` | `M` | エラー訂正レベル（L / M / Q / H） |
| `--dark` | `#000000` | QRコード（暗色部分）の色 |
| `--light` | `#ffffff` | 背景色 |
| `--border` | `4` | 余白サイズ（モジュール数） |

### エラー訂正レベルの目安

| レベル | 復元可能率 | 用途 |
|---|---|---|
| L | 約7% | データ量を小さくしたいとき |
| M | 約15% | 一般用途（デフォルト） |
| Q | 約25% | 汚れや破損が想定される環境 |
| H | 約30% | ロゴ重ねなど一部を隠す場合 |

## 使用例

```bash
# 高解像度で出力
python qrgen.py "https://example.com" --scale 20

# 色をカスタマイズ
python qrgen.py "https://example.com" --dark "#003366" --light "#ffffff"

# エラー訂正レベルを上げる
python qrgen.py "https://example.com" --error H

# 余白を広くする
python qrgen.py "https://example.com" --border 8
```

## 動作確認

生成された `.svg` ファイルはブラウザで開くか、印刷プレビューで確認できます。
# qrcode-generator
