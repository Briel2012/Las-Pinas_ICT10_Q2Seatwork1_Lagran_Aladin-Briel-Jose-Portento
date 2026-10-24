from pyscript import document 

def candidate_checker(e):
    club_members = {"kenzo cutamora" , "zach natividad" , "keon cutamora" , "arturo santos" , "jack sabitsana" , "kaizen sy" , "briel lagran"}

    f_name = document.getElementById("first name").value
    l_name = document.getElementById("last name").value
    candidate = f_name + '' + l_name 
    member_checker = candidate.lower() in club_members

    messages = (f'Sorry... {candidate}, your name is not on the list.' ,  
                f'Congratualations! {candidate}, you are part of the basketball varisty.')

    document.getElementById('result').innerHTML = messages(member_checker)