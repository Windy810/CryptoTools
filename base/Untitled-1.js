var strIn = "怦恺恮恫怦恗恴悁恴怵恲恾恼恴悂怳悃恷恴恬悄恽恀恲怿恳恴怽恪恵恀恐恶恀悂悊恂恲恂恱恇恂恁恁恇恆恰恄恄恆恇恱恂恄恀恀恵恲恳恆恃恇恅恵恃恴恵恈悌怵怴恞怲怲怴怵恟怰怲怮怮恣恠恡怴怱怵怳";
for (offset = -50; offset < 1000; offset++) {
    // console.log(i)
    var strOut = "", nCode;
    for (var i = 0; i < strIn.length; i++) {
        nCode = strIn.charCodeAt(i);
        if (nCode == 13) // \r
            strOut += "\r"; // do nothing
        else if (nCode == 10) // \n
            strOut += "\n"
        else if (nCode == 32) // space
            strOut += " ";
        else
            strOut += String.fromCharCode(strIn.charCodeAt(i) + offset);
    }
    console.log(strOut)
}