import arcade

class TextViewer(arcade.Window):

    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.screenWidth = SCREEN_WIDTH
        self.screenHeight = SCREEN_HEIGHT
        self.screenTitle = SCREEN_TITLE

        arcade.set_background_color(arcade.csscolor.BLACK)

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """
        pass

    def on_update(self, delta_time):
         """ Movement and game logic """
         pass

    def on_draw(self):
        """ Render the screen. """

        arcade.start_render()

         # Code to draw the screen goes here
        textSize1 = arcade.draw_text(text="Hello World", start_x=0, start_y=self.screenHeight, color=arcade.csscolor.BISQUE, font_size=20, anchor_x="left", anchor_y="top")
        textSize2 = arcade.draw_text(text="Hello World", start_x=243, start_y=self.screenHeight, color=arcade.csscolor.BISQUE, font_size=20, anchor_x="left", anchor_y="top")
        textSize1 = arcade.draw_text(text="Hello World", start_x=0, start_y=self.screenHeight-40, color=arcade.csscolor.BISQUE, font_size=20, anchor_x="left", anchor_y="top")
        textSize2 = arcade.draw_text(text="Hello World", start_x=243, start_y=self.screenHeight-40, color=arcade.csscolor.BISQUE, font_size=20, anchor_x="left", anchor_y="top")
        textSize2 = arcade.draw_text(text="Hello World", start_x=243+243, start_y=self.screenHeight, color=arcade.csscolor.BISQUE, font_size=20, anchor_x="left", anchor_y="top")
        textSize1 = arcade.draw_text(text="Hello World", start_x=243+243, start_y=self.screenHeight-40, color=arcade.csscolor.BISQUE, font_size=20, anchor_x="left", anchor_y="top")
        
        

def main():
    SCREEN_WIDTH = 600
    SCREEN_HEIGHT = 400
    SCREEN_TITLE = "Text"

    window = TextViewer(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()

    
