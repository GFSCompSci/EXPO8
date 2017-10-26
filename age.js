var age = prompt("How many years old are you?");

var secondsInAMinute = 60;
var minutesInAnHour = 60;
var secondsInAnHour = secondsInAMinute * minutesInAnHour;

var hoursInADay = 24;
var secondsInADay = secondsInAnHour * hoursInADay;
secondsInADay;

var daysInAYear = 365;
var secondsInAYear = secondsInADay *daysInAYear;
secondsInAYear;

var agesec = age * secondsInAYear;

alert("You are " + agesec + " seconds old.");
