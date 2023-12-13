// Colourize button is disabled until all fields are filled

// Get references to the input field and button
const inputPath = document.getElementById("input_text");
const outputPath = document.getElementById("output_text");
const colourizeButton = document.getElementById("button_colourize");

// flags are true for text fields that have content
var hasIn = false;
var hasOut = false;

// add an event listener for the input-field event
inputPath.addEventListener("input", () => {
  if (inputPath.value.length > 0) {
    hasIn = true;
  } else {
    hasIn = false;
  }
  // if both text fields have content, activate button
  canColourize();
});

// add an event listener for the output-field event
outputPath.addEventListener("input", () => {
  if (outputPath.value.length > 0) {
    hasOut = true;
  } else {
    hasOut = false;
  }
  // if both text fields have content, activate button
  canColourize();
});

function canColourize() {
  if (hasIn == true && hasOut == true) {
    colourizeButton.disabled = false;
  } else {
    colourizeButton.disabled = true;
  }
}