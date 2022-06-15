# flags of the world quiz
import random 
import json
from PIL import Image
import glob
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import matplotlib.image as mpimg
figure(figsize=(1,1), dpi=300)
countriesDICT = json.load(open('countries.json'))
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'
score = 0
count = 0 
image_list = [] 
for image in glob.glob('png1000px/*.png'):
    i = Image.open(image)
    image_list.append(i) 
print(color.BOLD + color.DARKCYAN + '\nFLAG QUIZ\n' + color.END)
def flagQuiz():
    global score, count
    uniqueCountries = random.sample(list(countriesDICT.items()),4)
    randList = random.sample([0,1,2,3], 4)
    print('1.',uniqueCountries[randList[0]][1],'\n'
            '2.',uniqueCountries[randList[1]][1],'\n'
            '3.',uniqueCountries[randList[2]][1],'\n'
            '4.',uniqueCountries[randList[3]][1],'\n')
    optionsDict = {1:uniqueCountries[randList[0]][1],2:uniqueCountries[randList[1]][1],3:uniqueCountries[randList[2]][1],4:uniqueCountries[randList[3]][1]}
    imgplot = plt.imshow(mpimg.imread('png1000px/'+str(uniqueCountries[0][0].lower())+'.png'))    
    plt.axis('off')
    plt.show()
    while True:
        try:
            playerGuess = input('Guess (enter "n" to exit): ')
            if playerGuess == 'n':
                print('\n' + color.BOLD + color.BLUE + 'Final Score: ' + str(score) + '/' + str(count) + color.END)
                exit()
            elif int(playerGuess) < 0:
                raise ValueError
            elif int(playerGuess) > 4:
                raise ValueError
            count += 1
            break
        except ValueError:
            print(color.YELLOW + 'Guess must be between 1 & 4' + color.END)
    if optionsDict[int(playerGuess)] == uniqueCountries[0][1]:
        score += 1     
        print(color.GREEN + color.BOLD + '\n' + uniqueCountries[0][1] + color.END, '\n' + 
        color.BLUE + 'Score: ' + str(score) + '/' + str(count) + color.END)
    else:
        print(color.RED + color.BOLD + '\n' + optionsDict[int(playerGuess)] + color.END, '\n' +
        color.GREEN + color.BOLD + uniqueCountries[0][1] + color.END, '\n' + 
        color.BLUE + 'Score: ' + str(score) + '/' + str(count) + color.END)
    flagQuiz()        
flagQuiz()