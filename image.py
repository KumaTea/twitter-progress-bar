# Ref: https://stackoverflow.com/a/22650239/10714490


from coord import *
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont


progress_path = 'img/progress.png'
# progress_path = 'img/color-wheel.png'
head_path = 'img/char.png'
back_path = 'img/back.png'
original_path = 'img/original.jpg'
now = datetime.now()
repo_link = 'git.io/tprog'
black_rgba = (0, 0, 0, 255)


def gen_progress_image(ppl, xrange=200, yrange=200):
    progress = Image.open(progress_path)
    if not progress.mode == 'RGBA':
        progress = progress.convert('RGBA')
    progress_array = np.asarray(progress)
    polygon = [(i[0], i[1]) for i in process_polygon(calc_polygon(calc_coord(ppl), xrange, yrange))]

    mask_progress = Image.new('L', progress.size, 0)
    # L: 8-bit pixels, black and white
    # https://pillow.readthedocs.io/en/stable/handbook/concepts.html#concept-modes

    ImageDraw.Draw(mask_progress).polygon(polygon, outline=1, fill=1)
    mask = np.array(mask_progress)
    mask = mask*255  # Alpha / transparency

    # assemble new image (uint8: 0-255)
    new_progress_array = np.empty(progress_array.shape, dtype='uint8')

    # colors (three first columns, RGB)
    new_progress_array[:, :, :3] = progress_array[:, :, :3]

    # This loop makes the mask follows the original image for the transparency values
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            if mask[i][j] == 255:
                mask[i][j] = progress_array[:, :, 3][i][j]
    # mask = [[progress_array[:, :, 3][i][j] if mask[i][j] == 255 else mask[i][j] for j in range(len(mask[i]))] for i in range(len(mask))]

    # transparency (4th column)
    new_progress_array[:, :, 3] = mask

    new_progress = Image.fromarray(new_progress_array, "RGBA")

    return new_progress


def gen_profile_image(progress, total_ppl, font_size=16, ppl=None, selenium=True):
    # original = Image.open(original_path)
    original = Image.open(back_path)
    profile = Image.new("RGBA", original.size)
    profile = Image.alpha_composite(profile, Image.open(back_path).convert('RGBA'))
    profile = Image.alpha_composite(profile, progress)
    profile = Image.alpha_composite(profile, Image.open(head_path).convert('RGBA'))

    txt = Image.new("RGBA", original.size, (255, 255, 255, 0))
    fnt = ImageFont.truetype('calibri.ttf', font_size)
    fnt2 = ImageFont.truetype('calibri.ttf', font_size+8)
    fnt3 = ImageFont.truetype('calibri.ttf', font_size+4)

    draw = ImageDraw.Draw(txt)

    date = now.strftime('%Y-%m-%d')
    time = now.strftime('%H:%M:%S')
    draw.text((5, 5), date, font=fnt, fill=black_rgba)
    draw.text((10, 5+font_size), time, font=fnt, fill=black_rgba)

    draw.text((350, 5), str(total_ppl), font=fnt2, fill=black_rgba)

    draw.text((5, 355), f'src:\n{repo_link}', font=fnt3, fill=(255, 128, 0, 255))

    # ppl should be int if given
    if not ppl:
        ppl = int(str(total_ppl)[-2:])
    if ppl == 0:
        ppl = 100
    draw.text((350, 5+font_size+8), f'{ppl}%', font=fnt2, fill=black_rgba)

    if selenium:
        method = '● Selenium\n○ API'
    else:
        method = '○ Selenium\n● API'
    draw.text((325, 365), method, font=fnt, fill=black_rgba)

    profile = Image.alpha_composite(profile, txt)

    return profile
