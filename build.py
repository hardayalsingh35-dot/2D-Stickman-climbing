import pathlib
S = pathlib.Path('/home/user/src')
out = pathlib.Path('/home/user')
stick = (S/'stickman.js').read_text()

def page(title, css, body, js, extra_head=""):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no">
<title>{title}</title>
{extra_head}
<style>
{css}
</style>
</head>
<body>
{body}
<script>
{stick}
</script>
<script>
{js}
</script>
</body>
</html>
"""

(out/'game.html').write_text(page(
    "Stickman Climber",
    (S/'game.css').read_text(), (S/'game.body.html').read_text(), (S/'game.js').read_text()))

(out/'animations.html').write_text(page(
    "Stickman Climbing — Animation Set",
    (S/'anim.css').read_text(), (S/'anim.body.html').read_text(), (S/'anim.js').read_text()))
print("built", [p.name for p in out.glob('*.html')])
