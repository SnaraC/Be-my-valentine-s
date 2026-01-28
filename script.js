// Function to show the next screen with Yes and No buttons
function showNext() {
    document.getElementById("click-button").style.display = "none"; // Hide the "Click Me" button
    document.getElementById("next-screen").style.display = "block"; // Show the next screen
}

// Function to handle Yes and No responses
function showResponse(answer) {
    const responseMessage = document.getElementById("response-message");
    const funnyImage = document.getElementById("funny-image");
    const sadImage = document.getElementById("sad-image");
    
    // Hide both images initially
    funnyImage.style.display = "none";
    sadImage.style.display = "none";
    
    if (answer === 'yes') {
        responseMessage.innerHTML = "I Love You!";
        funnyImage.style.display = "block"; // Show the funny picture for Yes
    } else {
        responseMessage.innerHTML = "Oh no!"; // Message for No
        sadImage.style.display = "block"; // Show the sad picture for No
    }

    document.getElementById("next-screen").style.display = "none"; // Hide the next screen
    document.getElementById("response-screen").style.display = "block"; // Show the response screen
}

// Function to go back to the initial state
function goBack() {
    document.getElementById("response-screen").style.display = "none"; // Hide the response screen
    document.getElementById("next-screen").style.display = "block"; // Show the next screen with Yes and No buttons
}