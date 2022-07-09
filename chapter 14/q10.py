
import random
def main():
    correct = 0
    state_capitals = {'Alabama' : 'Montgomery',	
        'Alaska' : 'Juneau',
        'Arizona' : 'Phoenix',	
        'Arkansas' : 'Little Rock',	
        'California' : 'Sacramento',	
        'Colorado' : 'Denver',	
        'Connecticut' : 'Hartford',	
        'Delaware' : 'Dover',	
        'Florida' : 'Tallahassee',	
        'Georgia' : 'Atlanta',	
        'Hawaii' : 'Honolulu',	
        'Idaho' : 'Boise',	
        'Illinois' : 'Springfield',	
        'Indiana' : 'Indianapolis',	
        'Iowa' : 'Des Moines',	
        'Kansas' : 'Topeka',	
        'Kentucky' : 'Frankfort',	
        'Louisiana' : 'Baton Rouge',	
        'Maine' : 'Augusta',	
        'Maryland' : 'Annapolis',	
        'Massachusetts' : 'Boston',	
        'Michigan' : 'Lansing',	
        'Minnesota' : 'Saint Paul',	
        'Mississippi' : 'Jackson',	
        'Missouri' : 'Jefferson City',	
        'Montana' : 'Helena',	
        'Nebraska' : 'Lincoln',	
        'Nevada' : 'Carson City',	
        'New Hampshire' : 'Concord',	
        'New Jersey' : 'Trenton',	
        'New Mexico' : 'Santa Fe',	
        'New York' : 'Albany',	
        'North Carolina' : 'Raleigh',	
        'North Dakota' : 'Bismarck',	
        'Ohio' : 'Columbus',	
        'Oklahoma' : 'Oklahoma City',	
        'Oregon' : 'Salem',	
        'Pennsylvania' : 'Harrisburg',	
        'Rhode Island' : 'Providence',	
        'South Carolina' : 'Columbia',	
        'South Dakota' : 'Pierre',	
        'Tennessee' : 'Nashville',	
        'Texas' : 'Austin',	
        'Utah' : 'Salt Lake City',	
        'Vermont' : 'Montpelier',	
        'Virginia' : 'Richmond',	
        'Washington' : 'Olympia',	
        'West Virginia' : 'Charleston',	
        'Wis consin' : 'Madison',	
        'Wy o ming' : 'Cheyenne'}
    
    statesName = list(state_capitals.keys())
    random.shuffle(statesName)
    for states in statesName:
        answer = input(f'What is the capital of {states}? : ').strip().lower()
        if answer == state_capitals[states].lower():
            print('Your answer is correct')
            correct +=1
        else:
            print(f'Correct answer should be {state_capitals[states]}')
    
    print(f'Total score : {correct}')

main()
    


