from cv2 import imread, resize,imshow,waitKey,destroyAllWindows,imwrite
from os import getcwdb

class ImageConverter : 

    def imageColorConverter(self,image_path,image_color):
        try:
            self.img = imread(image_path, image_color)
        except Exception as e:
            print(f"Error: {str(e)}")
            return
        if self.img is None:
            print("Error: Image not loaded.")
            return
        
    def displayImage(self,image_path,image_color=1):
        ImageConverter.imageColorConverter(self,image_path,image_color)
        window_name=input("Enter name of the image ") or "image"
        imshow(window_name, self.img)
        waitKey(0)
        destroyAllWindows()
        if(image_color==1):
            return
        save = input("Enter 's' to save the image ") 
        if save.lower() =='s':
            ImageConverter.saveImage(self,window_name)

    def saveImage(self,window_name):
            save_path =getcwdb()
            save_path = save_path.decode("utf-8").replace('\\',"/")+f"/{window_name}_black_and_white_image.jpg"
            print(f"Saving image to {save_path}")
            imwrite(save_path, self.img)
            print("Image saved successfully.")

    def imgConvert(self,image_path,width,height,character_set=" .:-=+*#%@"):
        ImageConverter.imageColorConverter(self,image_path,0)
        self.resized_img = resize(self.img, (width, height))
        ascii_art = []
        num_chars = len(character_set)
        for i in range(height):
            line = ""
            for j in range(width):
                pixel_value = self.resized_img[i, j]
                char_index = int((pixel_value / 255) * (num_chars - 1))
                line += character_set[char_index]
            ascii_art.append(line)

        return "\n".join(ascii_art)


def main():
    print(getcwdb())
    converter = ImageConverter()
    while True:
        choice = int(input("Choose:\n1:To Display Image\n2:To Display Image in Black and white\n3:To Convert Image into ASCII\n4:To Exit\n") or 0)
        match(choice):
            case 1:
                path=input("Enter image path: ")
                converter.displayImage(path)
            case 2:
                path=input("Enter image path: ")
                converter.displayImage(path,0)
            case 3:
                path=input("Enter image path: ")
                width=int(input("Enter width: "))
                height=int(input("Enter height: "))
                art=converter.imgConvert(path,width,height)
                print(art)
            case 4:
                print("Exiting...")
                break
            case _:
                print("Invalid choice. Please choose between 1-4.")

if __name__ == '__main__':
    main()