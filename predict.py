
from cog import BasePredictor, Input, Path
from PIL import Image, ImageEnhance, ImageOps, ImageFilter

class Predictor(BasePredictor):
    def predict(
        self,
        image: Path = Input(description="Input image"),
        style: str = Input(description="Style: anime, pixar, comic, ghibli, realistic_cartoon", default="anime")
    ) -> Path:
        img = Image.open(image).convert("RGB")

        if style == "anime":
            img = img.filter(ImageFilter.CONTOUR)
        elif style == "pixar":
            enhancer = ImageEnhance.Color(img)
            img = enhancer.enhance(2.0)
        elif style == "comic":
            img = ImageOps.posterize(img, 3)
        elif style == "ghibli":
            img = ImageEnhance.Brightness(img).enhance(1.2)
        elif style == "realistic_cartoon":
            img = ImageOps.equalize(img)

        output_path = "/tmp/cartoonized.png"
        img.save(output_path)
        return Path(output_path)
