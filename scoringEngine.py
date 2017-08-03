#TEAM NAMES
team1= 'Dragons'
team2= 'Thunder'
team3= 'Boneless'
team4= 'Pizza'
team5= 'Taco'
team6= 'Nugget'
lstTeams= [team1,team2,team3,team4,team5,team6]
#****************************************************************************
#Default Settings
maxScore= 300
timeScore= 0
obstacleEasy= 5
obstacleMedium= 10
obstacleHard= 15
ground = -10
OutputFile= 'score_saver.txt'
teamScores=[[team1, 0],[team2, 0],[team3, 0],[team4, 0],[team5, 0],[team6, 0]]

def showScores(teamScores):
    for team in teamScores:
        print(team)
        #copyToFile(OutputFile, team) DOES NOT WORK
def copyToFile(OutputFile,text):
    'Writes the scores line by line to a txt file'
    fin= open(OutputFile, 'w')
    fin.write(str(text))
    fin.close()
def calcScores():
    #Gather User Input
    raceTime= int(input('Enter run time in seconds: '))
    easy=int(input('How many easy obstacles?: '))
    medium=int(input('How many medium obstacles?: '))
    hard=int(input('How many hard obstacles?: '))
    penalty =int(input('How many times do they hit the ground?: '))
    #Calculate Scores
    penaltyGrnd = ground*penalty
    timeScore = maxScore - raceTime
    easyScore=obstacleEasy*easy
    mediumScore=obstacleMedium*medium
    hardScore=obstacleHard*hard
    finalScore= timeScore+easyScore+mediumScore+hardScore+penaltyGrnd
    return finalScore
def updateScore(teamName):
    'updates the score for a given team'
    for team in teamScores:
        if team[0]== teamName:
            team[1] = calcScores()
    showScores(teamScores)
def main():
    'handles stuff'
    done= False
    teamName='sam'
    while not done:
        if teamName== '':
            done= True
        else:
            print('The teams are: ')
            for team in lstTeams:
                print(team)
            teamName= input('Enter Team Name: ')
            teamName= teamName.lower().capitalize()
            updateScore(teamName)


main()