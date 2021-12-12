def get_indexed_dict(movie_info):
    new = []
    months = {'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6}
    for i in range(len(movie_info)):
        
        new.append({ 'movie_name': movie_info[i]['movie_name'],
                    'start_date': movie_info[i]['start_date'],
                    'start_month': int(months[movie_info[i]['start_date'].split()[1]]),
                    'end_date': movie_info[i]['end_date']
                   })
    
    # soting by month
    newlist = sorted(new, key=lambda d: d['start_month'])
    return newlist

def ret_movie_list(movies):
    temp = {}
    new_movie_info = {}
    
    for i in range(len(movies)):
        for j in range(i+1,len(movies)):
            
            # month match.......................
            if movies[i]['start_date'].split()[1] == movies[j]['start_date'].split()[1] and movies[i]['end_date'].split()[1] == movies[j]['end_date'].split()[1]:
                #print(movies[i]['movie_name'],movies[j]['movie_name']+" ---> "+"month matched")
                
                if ( int(movies[i]['start_date'].split()[0]) > int(movies[j]['start_date'].split()[0]) ):
                    #print(movies[i]['movie_name'],movies[j]['movie_name']+" ---> "+" i movie start after j movie", "..............Done")
                    #seq.append({movies[i]['movie_name']:movies[j]['movie_name']})
                    
                    if movies[i]['movie_name'] not in temp:
                        temp[movies[i]['movie_name']] = [movies[j]['movie_name']]
                    else:
                        temp[movies[i]['movie_name']].append(movies[j]['movie_name'])
                    
                elif ( int(movies[i]['end_date'].split()[0]) < int(movies[j]['start_date'].split()[0]) ):
                    #print(movies[i]['movie_name'],movies[j]['movie_name']+" ---> "+" i movie end before j movie", "..............Done")
                    #seq.append({movies[i]['movie_name']:movies[j]['movie_name']})  
                    
                    if movies[i]['movie_name'] not in temp:
                        temp[movies[i]['movie_name']] = [movies[j]['movie_name']]
                    else:
                        temp[movies[i]['movie_name']].append(movies[j]['movie_name'])
                     
                else:
                    pass
                    #print(movies[i]['movie_name'],movies[j]['movie_name']+" ---> "+" i and j movie overlap each other")
            
            # only start month match , end month not match
            elif movies[i]['start_date'].split()[1] == movies[j]['start_date'].split()[1] and movies[i]['end_date'].split()[1] != movies[j]['end_date'].split()[1]:
                #print(movies[i]['movie_name'],movies[j]['movie_name']+" ---> ","start match end not match")
                if ( int(movies[i]['end_date'].split()[0]) < int(movies[j]['start_date'].split()[0]) ):
                    #print(movies[i]['movie_name'],movies[j]['movie_name']+" ---> "+" i movie finish befor j movie", ".............Done")
                    #seq.append({movies[i]['movie_name']:movies[j]['movie_name']})
                    
                    if movies[i]['movie_name'] not in temp:
                        temp[movies[i]['movie_name']] = [movies[j]['movie_name']]
                    else:
                        temp[movies[i]['movie_name']].append(movies[j]['movie_name'])
                else:
                    pass
                    #print(movies[i]['movie_name'],movies[j]['movie_name']+" ---> "+" i and j movie overlap each other")
            
            # no start end month matches
            elif movies[i]['start_date'].split()[1] != movies[j]['start_date'].split()[1] and movies[i]['end_date'].split()[1] != movies[j]['end_date'].split()[1]:
                #print(movies[i]['movie_name'],movies[j]['movie_name']+" --> "+"no month matches", "..........................Done")
                #seq.append({movies[i]['movie_name']:movies[j]['movie_name']})
                
                if movies[i]['movie_name'] not in temp:
                        temp[movies[i]['movie_name']] = [movies[j]['movie_name']]
                else:
                    temp[movies[i]['movie_name']].append(movies[j]['movie_name'])
    
    # getting corect sequence of movie for again
    for movie in movies:
        new_movie_info[movie['movie_name']] = {'start_date':movie['start_date'],'end_date':movie['end_date']}
                    
    return get_sequence(temp,new_movie_info)



def get_sequence(temp,new_movie_info):
    temp2 = {}

    length = 0
    li = []
    main_seq = []
    
    for key in temp:
        for i in range(0,len(temp[key])-1):

            # month match.......................
            if new_movie_info[temp[key][i]]['start_date'].split()[1] == new_movie_info[temp[key][i+1]]['start_date'].split()[1] and new_movie_info[temp[key][i]]['end_date'].split()[1] == new_movie_info[temp[key][i+1]]['end_date'].split()[1]:
                #print(key,new_movie_info[temp[key][i]],new_movie_info[temp[key][i+1]],"month match..................")

                if ( int(new_movie_info[temp[key][i]]['start_date'].split()[0]) > int(new_movie_info[temp[key][i+1]]['start_date'].split()[0]) ):
                    #print(key,new_movie_info[temp[key][i]],new_movie_info[temp[key][i+1]],"i movie start after j movie..............Done")
                    
                    if key not in temp2:
                        temp2[key] = [temp[key][i],temp[key][i+1]]
                    else:
                        temp2[key].append(temp[key][i])
                        temp2[key].append(temp[key][i+1])
                        
                elif ( int(new_movie_info[temp[key][i]]['end_date'].split()[0]) < int(new_movie_info[temp[key][i+1]]['start_date'].split()[0]) ):
                    #print(key,new_movie_info[temp[key][i]],new_movie_info[temp[key][i+1]],"i movie end before j movie..................Done")
                    
                    if key not in temp2:
                        temp2[key] = [temp[key][i],temp[key][i+1]]
                    else:
                        temp2[key].append(temp[key][i])
                        temp2[key].append(temp[key][i+1])
                else:
                    pass
                    #print(key,new_movie_info[temp[key][i]],new_movie_info[temp[key][i+1]],"i and j movie overlap each other")

            # only start month match , end month not match
            elif new_movie_info[temp[key][i]]['start_date'].split()[1] == new_movie_info[temp[key][i+1]]['start_date'].split()[1] and new_movie_info[temp[key][i]]['end_date'].split()[1] != new_movie_info[temp[key][i+1]]['end_date'].split()[1]:
                #print(key,new_movie_info[temp[key][i]],new_movie_info[temp[key][i+1]],"start match end not match")

                if ( int(new_movie_info[temp[key][i]]['end_date'].split()[0]) < int(new_movie_info[temp[key][i+1]]['start_date'].split()[0]) ):
                    #print(key,new_movie_info[temp[key][i]],new_movie_info[temp[key][i+1]],"i movie finish befor j movie.....DOne")
                    
                    if key not in temp2:
                        temp2[key] = [temp[key][i],temp[key][i+1]]
                    else:
                        temp2[key].append(temp[key][i])
                        temp2[key].append(temp[key][i+1])
                else:
                    pass
                    #print(key,new_movie_info[temp[key][i]],new_movie_info[temp[key][i+1]],"i and j movie overlap each other")

            # no start end month matches
            elif new_movie_info[temp[key][i]]['start_date'].split()[1] != new_movie_info[temp[key][i+1]]['start_date'].split()[1] and new_movie_info[temp[key][i]]['end_date'].split()[1] != new_movie_info[temp[key][i+1]]['end_date'].split()[1]:
                #print(key,new_movie_info[temp[key][i]],new_movie_info[temp[key][i+1]],"no month matches...........")
                
                if key not in temp2:
                    temp2[key] = [temp[key][i],temp[key][i+1]]
                else:
                    temp2[key].append(temp[key][i])
                    temp2[key].append(temp[key][i+1])
    
    # return proper sequence
    for key in temp2:
        if length < len(temp2[key]):
            length = len(temp2[key])
            li.append(key)
            main_seq.append(key)
    for movi in temp2[li[-1]]:
        main_seq.append(movi)
    
    main_seq = set(main_seq)
    return main_seq,len(main_seq)


if __name__ == "__main__":
   

    # Test Case 1
    movie_info = [ {'movie_name':'Bala',"start_date":'08 jan',"end_date":'28 jan'},
    {'movie_name':'Rock',"start_date":'20 jan',"end_date":'30 jan'},
    {'movie_name':'PolicyMaker',"start_date":'29 jan',"end_date":'16 feb'},
    {'movie_name':'Brave',"start_date":'02 feb',"end_date":'14 feb'},
    {'movie_name':'Race',"start_date":'15 feb',"end_date":'28 feb'},
    ]

    # test Case2
    movie_info3 = [{'movie_name': 'Dhoom', 'start_date': '25 mar','end_date': '18 apr'},
                {'movie_name': 'King', 'start_date': '29 apr', 'end_date': '10 jun'},
               {'movie_name': 'Run', 'start_date': '09 may', 'end_date': '2 jun'},
                {'movie_name': 'Bala', 'start_date': '08 jan','end_date': '28 jan'},
                {'movie_name': 'Rock', 'start_date': '20 jan', 'end_date': '30 jan'},
                {'movie_name': 'PolicyMaker', 'start_date': '29 jan', 'end_date': '16 feb'},
                {'movie_name': 'Brave', 'start_date': '02 feb',  'end_date': '14 feb'},
                {'movie_name': 'Race', 'start_date': '15 feb',  'end_date': '28 feb'},
                ]

    #test case 1
    new_movie_info1 = get_indexed_dict(movie_info)
    seq1, money1 = ret_movie_list(new_movie_info1)
    print(f"Test Case 1:\nsequence: {seq1}\nmoney: {money1} crore")

    #test case 2
    new_movie_info2 = get_indexed_dict(movie_info3)
    seq2, money2 = ret_movie_list(new_movie_info2)
    print(f"Test Case 2:\nsequence: {seq2}\nmoney: {money2} crore")


    
    
