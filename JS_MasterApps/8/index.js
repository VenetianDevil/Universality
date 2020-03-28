function getFullName(user){
    return user.firstname.concat(user.lastname);
}

function isMale(user){
    if(user.gender == 'male')
        return true;
    return false;
}

function isOfAge(user){
    if(user.age < 18)
        return false;
    return true;
}