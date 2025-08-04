function respond(action) {
  let phrase = '';
  if (action === 'yes') phrase = "Let’s get started, Commander.";
  if (action === 'learn') phrase = "Let’s explore your Codex first.";
  if (action === 'show') phrase = "Let’s show you how this all works.";
  const synth = window.speechSynthesis;
  const utter = new SpeechSynthesisUtterance(phrase);
  synth.speak(utter);
}
