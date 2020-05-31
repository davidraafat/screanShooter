#taking screans for each 100 ms 
from PIL import ImageGrab
import time 

# you should remove screans every time you restart the program
on = True;
count = 0;
while on :
    snapshot = ImageGrab.grab()
    #change your path as u like but after each \ make it \\
    save_path = 'C:\\Users\\David\\Desktop\\Screans\\';
    save_path += str(count) + ".jpg";
    snapshot.save(save_path);
    # time sleep by second so 0.1s = 100ms
    time.sleep(0.1);
    count+=1;