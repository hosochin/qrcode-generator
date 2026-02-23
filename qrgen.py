import argparse
import segno
import sys


def main():
    parser = argparse.ArgumentParser(description='QRコードをSVGで生成する')
    parser.add_argument('data', help='QRコードに埋め込むデータ（URLやテキスト）')
    parser.add_argument('-o', '--output', default='output.svg', help='出力ファイル名')
    parser.add_argument('--scale', type=int, default=10, help='スケール（デフォルト: 10）')
    parser.add_argument('--error', choices=['L', 'M', 'Q', 'H'], default='M', help='エラー訂正レベル')
    parser.add_argument('--dark', default='#000000', help='QRコードの色')
    parser.add_argument('--light', default='#ffffff', help='背景色')
    parser.add_argument('--border', type=int, default=4, help='余白サイズ（モジュール数）')
    args = parser.parse_args()

    qr = segno.make(args.data, error=args.error)
    qr.save(args.output, scale=args.scale, dark=args.dark, light=args.light, border=args.border)
    print(f'生成完了: {args.output}')


if __name__ == '__main__':
    main()
