const words = ["Unity", "Android", "WebDev", "Marketing"];
const animationDuration = 300; // in milliseconds
const delayBetweenLetters = 60; // in milliseconds
const delayBetweenWords = 1000; // in milliseconds
const container = document.getElementById("wordAnimation");
let currentWordIndex = 0;

function animateLetter(letter, delay) {
  return new Promise(resolve => {
    setTimeout(() => {
      letter.style.animation = "appear 0.5s forwards";
      resolve();
    }, delay);
  });
}

function eraseLetter(letter, delay) {
  return new Promise(resolve => {
    setTimeout(() => {
      letter.style.animation = "erase 0.5s forwards";
      resolve();
    }, delay);
  });
}

async function animateWord(word) {
  const wordElement = document.getElementById("currentWord");
  wordElement.innerHTML = ""; // Clear existing content

  for (let i = 0; i < word.length; i++) {
    const letter = document.createElement("span");
    letter.textContent = word[i];
    letter.className = "letter";
    letter.style.animationDuration = `${animationDuration}ms`;

    wordElement.appendChild(letter);

    await animateLetter(letter, i * delayBetweenLetters);
    await new Promise(resolve => setTimeout(resolve, animationDuration));
  }

  // Erase word
  for (let i = word.length - 1; i >= 0; i--) {
    await eraseLetter(wordElement.children[i], (word.length - i - 1) * delayBetweenLetters);
    await new Promise(resolve => setTimeout(resolve, animationDuration));
  }
}

async function startAnimation() {
  while (true) {
    await animateWord(words[currentWordIndex]);

    currentWordIndex = (currentWordIndex + 1) % words.length;

    // Delay before starting the next word
    await new Promise(resolve => setTimeout(resolve, delayBetweenWords));
  }
}

// Start the animation when the page loads
startAnimation();
