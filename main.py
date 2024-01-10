from Action import perform_action
from Comms import speak, listen, send_emails, chatgpt, test_chat_gpt
from fileutils import greeting
import asyncio


# Define the main function
def voice_command():
    bot_name = 'Jarvis'

    command = listen()

    # Check if the trigger word is present in the user's input
    while bot_name.lower() == command.lower():
        # Prompt the user for the next phrase
        speak("Yes sir, how can I assist you?")
        command = listen()
    if bot_name.lower() in command.lower():
        perform_action(command)
    return command


async def main():
    greeting()

    command = ''
    while True:
        if 'session' in command:
            return None
        command = voice_command()


if __name__ == "__main__":

    query = '''
    User:
Pretend you are an expert pickle ball coach. 
I have come to you as new student that has aspirations of going pro in a few years time. 

I am 39 years old and am in okay shape. 
I weigh 178 pounds. 

I don’t have any inhibitors or injuries

I am also autistic so I come from that mindset and can hyper focus on this at times

I am willing to do any drills and excercises
I do have some experience with strength training and conditioning including olympic lifting
My current level of fitness is moderate

for instance this was my last workout in the form of csv:

Date,DOW,Exercise,Reps,Weight,WeightUnits,Distance,DistanceUnits,Function,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,Box Jumps,5,,,24,in,activation,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,Box Jumps,5,,,30,in,activation,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,Box Jumps,5,,,30,in,activation,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,Front Squats,6,45,lbs,,,workout,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,Front Squats,6,95,lbs,,,workout,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,Front Squats,6,115,lbs,,,workout,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,Front Squats,6,135,lbs,,,workout,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,Rear Foot Elevated Split Squats,6,0,lbs,,,workout,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,Rear Foot Elevated Split Squats,6,45,lbs,,,workout,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,Rear Foot Elevated Split Squats,6,65,lbs,,,workout,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,Calf Raisers Machine,10,140,lbs,,,workout,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,Calf Raisers Machine,10,160,lbs,,,workout,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,Calf Raisers Machine,10,180,lbs,,,workout,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,jog,10,,,1,half-court pickleball laps,activation,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,side shuffle step sprints,10,,,,,Footwork and leg strength,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,ladder drills,10,,,,,Footwork and leg strength,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,but kicks,5,,,,,Footwork and leg strength,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,russian steps,5,,,,,Footwork and leg strength,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,high kneeds,5,,,,,Footwork and leg strength,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,forward sprints,10,,,,,Footwork and leg strength,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,backward sprints,10,,,,,Footwork and leg strength,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,line hops - side to side,100,,,,,Footwork and leg strength,,,,,,,,,,,,,,,,,,,
8/14/23,Mon,line hops - front to back,100,,,,,Footwork and leg strength,,,,,,,,,,,,,,,,,,,


I have up to 20 hours a week to dedicate to this (including workouts and training and practicing and games)

I have access to a top of the line gym with practically every equipment (including sauna, steam room, cold plunge, hot tub) and classes including: yoga, indoor cycling, etc.

I wear basketball shoes that I only wear while playing same shoes as here https://www.nike.com/t/lebron-witness-7-basketball-shoes-43zKtc/DM1123-004?nikemt=true&cp=31765401338_search_--x-20455850764---c-----9032951-1000966839-00196153734883&gclid=CjwKCAjwivemBhBhEiwAJxNWN_4KfU_u99yz57Dw0YrAYzHXVpRd1LmI1VvSJPdIDHnedjEOT5-uNhoC4K4QAvD_BwE&gclsrc=aw.ds

I currently play about 3-4 times a week for about a 2 hours for the last month
From a self evaluation based on https://usapickleball.org/tournaments/tournament-player-ratings/player-skill-rating-definitions/ I am a level 4.0 player

I usually play indoors
I am able to play with other people that around level 4.0 5 times a week

here is a csv of my skills in pickleball

Name,CurrentStrength (1-10),Desc
Traditional Topspin Serve,5,Serve with forward spin hit hard to baseline
Drop Slice Serve,6,Serve with backward spin that floats to basline and soft bounce
Slice Serve,5,Hit the ball with a slice serve
Cut Serve,3,Serve with side spin
Lob Serve,4,Hit the ball high and deep to the back court
Soft Serve,6,Hit the ball with a soft serve
Drop,3,Hit the ball low and short
Dive,8,Hit the ball from baseline that clears the net and then dives down with topspin
Cross-Court Drop,3,Hit the ball low and short to the opposite court
Overhead Drop Shot,5,Hit the ball high and short over the net
Lob,7,Hit the ball high and deep
Cross-Court Lob,7,Hit the ball high and deep to the opposite court
Dink Backspin,2,Dink with backspin
Dink Topspin,2,Dink with topspin
Push Shot,5,Hit the ball with a soft shot close to the net with no spin
Reset,2,
Chip,5,Hit the ball with a soft chip
Drop Volley,4,Hit the ball low and short over the net
Volley,7,Hitting the ball before it bounces
Half-Volley,3,Hit the ball after it bounces and before it reaches your knees
Underhand Volley,,Hit the ball with an underhand volley
Block,5,Hit the ball with a soft block
Overhead Smash,5,Hit the ball with power above the head
Drive,6,Hit the ball with power from the baseline
Cross-Court Drive,4,Hit the ball with power to the opposite court
Groundstroke,7,hitting off bounce hard
Pinch Shot,5,Hit the ball with an angled shot close to the net
Fade,4,Hit the ball with an angled shot away from the net
Slice,6,Hit the ball with backspin
Cut,2,Hit the ball with side spin
Backhand Clear,6,Hit the ball high and deep with a backhand shot

You should setup long-term and short-term goals to help me go pro

You are only a online, virtual, text-only coach
You have decided to do your best to make my aspirations a reality. 

ChatGPT:
To make your pro pickleball aspirations a reality, we will need to set some long-term and short-term goals. For the long-term, our goal is to be competing at a professional level within the next few years. We will need to focus on improving your overall strength, fitness, and skill level in order to achieve this goal. 

For the short-term, our goal is to improve your physical fitness and pickleball skills. We will focus on strength training (including Olympic lifting), conditioning, and drills to help develop your pickleball skills. We will also need to focus on improving your footwork, agility, and stamina, as these are all key components to becoming a successful pickleball player. 

User: come up with a one-week schedule including:
 * nutrition on a budget
 * workout schedule
 * practice schedule
 * recovery schedule
Please be as detailed as possible
Make each day different
make sure there are recovery days from working out
list the name of the pickleball drills and exercises
list the days to play pickleball games with other people
ensure that no more than 4 total hours are spent on recovery, excercise, practicing, and training combined
make sure that the same muscle groups are not exerted 2 days in a row
list the name of the workout exercises to be performed each day
complete with day of the week and time for each activity
    '''
    query = """
list 100 workout exercises grouped by part of body (back, legs, shoulders, abs, chest, arms):
with the part of body that the excercise will strengthen with the following options: back, legs, shoulders, abs, chest, arms:
These exercises should be geared for playing pickleball:
Order them by priority in how they will prepare me for playing pickleball:
put in the form of csv:
for example:
1, exercise1, bodypart1,
2, exercise2, bodypart2,
"""

    query = '''
pretend like you are an expert data analyst charged with running an analysis on some marketing data for subscriptions, 
visits, and trials.
you have setup the basic structure of the project in a directory on github with some documentation about assumuptions,
steps taken, answers to some questions that they had, requirements, and some recommendations for some further analysis.
you also have a src directory with some basic python programs that you used to perform the analysis.
you also have 2 data files with the tables in csv files.
you also have some output files with the outputs of your programs that you used as the basis for your analysis.
you have also have setup a virtual environment and have a Requirements.txt file.
what should go in the README.md file for the project? 
        
    '''

    query = """
    This function:
def read_css_file(file):
    with open(file, 'r') as css:
        data = css.read()
        css_lines = data.split(';')
        formatted_css = []

        for line in css_lines:
            if '@import' in line:
                formatted_css.append(line)
            else:
                line_items = line.split('{')
                selector = line_items[0].strip()
                value_pairs = line_items[1].split(',')

                for pair in value_pairs:
                    pair_items = pair.split(':')
                    key = pair_items[0].strip()
                    value = pair_items[1].strip()
                    formatted_css.append(f'{selector} {key}: {value};')

    with open('formatted_css.css', 'w') as out:
        out.write('\n'.join(formatted_css))


read_css_file('ippa/www.ppatour.com/wp-content/cache/min/1/eyq3mdr_ver_1699288694.css')
when reading this file:
    @import url('../../../../../p.typekit.net/p_s_1_k_eyq3mdr_ht_tk_f_25308.39722.39725_a_2953780_app_typekit_e_css.css');@font-face{font-family:"industry";src:url('../../../../../use.typekit.net/af/e48727/00000000000000007735a648/30/l_primer_7cdcb44be4a7db8877ffa5c0007b8dd865b3bbc383831fe2ea177f62257a9191_fvd_n8_v_3') format("woff2"),url('../../../../../use.typekit.net/af/e48727/00000000000000007735a648/30/d_primer_7cdcb44be4a7db8877ffa5c0007b8dd865b3bbc383831fe2ea177f62257a9191_fvd_n8_v_3') format("woff"),url('../../../../../use.typekit.net/af/e48727/00000000000000007735a648/30/a_primer_7cdcb44be4a7db8877ffa5c0007b8dd865b3bbc383831fe2ea177f62257a9191_fvd_n8_v_3') format("opentype");font-display:swap;font-style:normal;font-weight:800;font-stretch:normal}@font-face{font-family:"unit-rounded";src:url('../../../../../use.typekit.net/af/0e6a34/00000000000000007735ba5a/30/l_primer_7cdcb44be4a7db8877ffa5c0007b8dd865b3bbc383831fe2ea177f62257a9191_fvd_n7_v_3') format("woff2"),url('../../../../../use.typekit.net/af/0e6a34/00000000000000007735ba5a/30/d_primer_7cdcb44be4a7db8877ffa5c0007b8dd865b3bbc383831fe2ea177f62257a9191_fvd_n7_v_3') format("woff"),url('../../../../../use.typekit.net/af/0e6a34/00000000000000007735ba5a/30/a_primer_7cdcb44be4a7db8877ffa5c0007b8dd865b3bbc383831fe2ea177f62257a9191_fvd_n7_v_3') format("opentype");font-display:swap;font-style:normal;font-weight:700;font-stretch:normal}@font-face{font-family:"unit-rounded";src:url('../../../../../use.typekit.net/af/ce697c/00000000000000007735ba5d/30/l_primer_7cdcb44be4a7db8877ffa5c0007b8dd865b3bbc383831fe2ea177f62257a9191_fvd_n3_v_3') format("woff2"),url('../../../../../use.typekit.net/af/ce697c/00000000000000007735ba5d/30/d_primer_7cdcb44be4a7db8877ffa5c0007b8dd865b3bbc383831fe2ea177f62257a9191_fvd_n3_v_3') format("woff"),url('../../../../../use.typekit.net/af/ce697c/00000000000000007735ba5d/30/a_primer_7cdcb44be4a7db8877ffa5c0007b8dd865b3bbc383831fe2ea177f62257a9191_fvd_n3_v_3') format("opentype");font-display:swap;font-style:normal;font-weight:300;font-stretch:normal}.tk-industry{font-family:"industry",sans-serif}.tk-unit-rounded{font-family:"unit-rounded",sans-serif}
returned this error:
Traceback (most recent call last):
  File "/Users/WCheaq/ippa/scratch_6.py", line 39, in <module>
    read_css_file('ippa/www.ppatour.com/wp-content/cache/min/1/eyq3mdr_ver_1699288694.css')
  File "/Users/WCheaq/ippa/scratch_6.py", line 27, in read_css_file
    value_pairs = line_items[1].split(',')
                  ~~~~~~~~~~^^^
IndexError: list index out of range
fix the function to account for this:
    
    """
    print(test_chat_gpt(prompt=query, max_tokens=2500))

