# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

When I opened the  Glitchy game and ran it for the first time, I picked a number between 1 and 100 and noticed the history output was a little bit off. The attempts were also a little bit off. the prompts also show the wrong information.

- List at least two concrete bugs you noticed at the start 
  (for example: "the secret number kept changing" or "the hints were backwards").

two concrete bugs I noticed was that the prompts within the code in the if statement blocks were switched around from the code to low! GO LOWER! and the to high, GO HIGHER! Another one was that the str(guess) code was wrong. It should be int for integer because the game returns a number, not a letter. During the game, I expected it to have a couple of bugs but it actually looks confusing for a beginner playing this glitchy game if they never used technology before. 

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

AI tools that I used on this project were Claude. I used AI as a teamate by going to my AI, and working together to solving bugs and understanding the logic behind those bugs. One example of an AI suggestion that was correct was making an import command at the top on line 3 to moving my logic functions. I verified the results by double checking to making sure everything is right and that none of the code looks off, and everything looks correct, even afer I ran the game 2-3 times. The AI suggested this code to make things a bit more organized. I verified the result in the code and game by testing the game myself and having a family member trying to play the game. 

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

How I verified my repairs is doing code reviews, asked AI to do pytest in the test_game_logic, tested a couple of bugs like parse_guess, update_score, and atempt_number functions,and I ran the test_game_logic.py and got an 11/11 to passing manually with the help from claude code. 

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
- What change did you make that finally gave the game a stable secret number?

The secret number kept changing in the original app because it kept on generating the secret number on every rerun within the game. Streamlit session code block allows the number to generate only once within the game. If someone has never used streamlit I would explain it to them like they were five years old. I would explain it to them that streamlit rerun gets erased and redrawn everytime someone does something like clicking a number or a script, or anything. Session state within the game means that a number will always have the same value, no matter how many times Streamlit reruns the app. A session state is something that never gets wiped out. 

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit or strategy from this project that I want to reuse in the future is having AI as my partner to colaborating and helping me debug my code and understanding the logic at the same time, in future labs/ projects I want to learn more about what I am doing while debugging. I wanna learn how to also set up my projects correctly before getting started to anything. One thing I would do differently next time I would work on AI is maybe being a little more dependent on AI while debugging my code. I have never cheated with AI, but usually I learn best to my knowledge by having things I am learning being repeated to myself, and then applying it as my own to other assignments. During this project, my different perspective views on AI when it generates code, as it always has been before I even started this project is that AI is not a replaceable machine that can write every single code for you. AI is only there for you to help assist, and debug code, or anything else you ask for. AI like chat GPT, or Claude code, or even copilot can be help to your assistance with technology, when you are direct, and specific with your project while running the code. AI did give me a few wrong turns like leftover bugs, and everything but it was a pretty easy fix with AI around!!
