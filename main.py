from PIL import Image, ImageFont, ImageDraw
import numpy as np
import csv
import os, tkinter, tkinter.filedialog, tkinter.messagebox, tkinter.filedialog

def main():

    # 【原画選択】
    # ファイル選択ダイアログの表示
    root = tkinter.Tk()
    root.withdraw()
    # ファイルタイプを制限　fTyp = [("","*")]
    fTyp = [("", "*.png")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    tkinter.messagebox.showinfo('領収書発行システム', '画像テンプレートを選択してください！')
    img_src = tkinter.filedialog.askopenfilename(filetypes=fTyp, initialdir=iDir)

    # 【CSV選択】
    # ファイル選択ダイアログの表示
    root = tkinter.Tk()
    root.withdraw()
    # ファイルタイプを制限　fTyp = [("","*")]
    fTyp = [("","*.csv")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    tkinter.messagebox.showinfo('領収書発行システム', 'CSVを選択してください！')
    csv_src = tkinter.filedialog.askopenfilename(filetypes = fTyp,initialdir = iDir)

    # 【保存先選択】
    # ファイル選択ダイアログの表示
    root = tkinter.Tk()
    root.withdraw()
    # ファイルタイプを制限　fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    tkinter.messagebox.showinfo('領収書発行システム', '保存先を選択してください！')
    save_src = tkinter.filedialog.askdirectory(initialdir = iDir)

    # CSV -> List
    with open(csv_src, encoding='cp932') as f:
        reader = csv.reader(f)
        l = [row for row in reader]
    # List総数
    total = len(l)
    cnt = 0

    # フォント指定
    font_path = "./font/ヒラギノ角ゴシック W5.ttc"
    font_size_name = 80
    font_size_date = 75
    font_size_subjects = 45
    img_save_size = 2480, 1748

    # 【テキスト入れ】
    # row[0] => 購入番号
    # row[1] => 購入日時
    # row[4] => 宛名
    # row[5] => 勘定科目
    for row in l:
        # 処理状況出力
        cnt += 1
        print(str(round(cnt/total*100, 2)) + "%(" + str(cnt) + "/" + str(total) + ")")

        # img = Image.fromarray(img)  # cv2(NumPy)型の画像をPIL型に変換
        img = Image.open(img_src)
        img.thumbnail(img_save_size)
        draw = ImageDraw.Draw(img)  # 描画用のDraw関数を用意

        # PILでフォントを定義
        font_name = ImageFont.truetype(font_path, font_size_name)
        font_date = ImageFont.truetype(font_path, font_size_date)
        font_sbj = ImageFont.truetype(font_path, font_size_subjects)

        # ピクセルサイズを取得
        w_name, h_name = draw.textsize(row[4], font_name)
        w_date, h_date = draw.textsize(row[1], font_date)
        w_sbj, h_sbj = draw.textsize(row[5], font_sbj)

        # テキストを描画（位置、文章、フォント、文字色(BGR+α)を指定）
        draw.text((500-w_name/2, 430-h_name/2), row[4] + "　様", font=font_name, fill=(0, 0, 0, 0))
        draw.text((1990-w_date/2, 430-h_date/2), "発行日：" + (row[1])[:9], font=font_date, fill=(0, 0, 0, 0))
        draw.text((604, 931), "但し " + row[5], font=font_sbj, fill=(0, 0, 0, 0))

        # img.thumbnail(img_save_size)
        img.save(save_src + "/TANABATA-SKYLANTERN-FESTIVAL-2021_exp" + str(row[0]) + ".jpg", dpi=(300, 300))


    # 完了通知
    tkinter.messagebox.showinfo('領収書発行システム', '完了しました！\n')



main()