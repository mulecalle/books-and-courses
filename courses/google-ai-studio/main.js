import { GoogleGenAI } from "@google/genai";
import { writeToFile, readFromFile } from "./utils/fileUtils.js";
import { sleep } from "./utils/time.js";

const GEMINI_API_KEY = process.env.GEMINI_API_KEY;
const ai = new GoogleGenAI({apiKey: GEMINI_API_KEY});
const prompt = await readFromFile('./prompt.md');

// 1. Start the Deep Research Agent
const initialInteraction = await ai.interactions.create({
    input: prompt,
    agent: 'deep-research-pro-preview-12-2025',
    background: true,
});

console.log(`Research started. Interaction ID: ${initialInteraction.id}`);

// 2. Poll for results
while (true) {
    const interaction = await ai.interactions.get(initialInteraction.id);
    console.log(`Status: ${interaction.status}`);

    if (interaction.status === 'completed') {
        console.debug('\nInteraction ended, now writing a file');
        await writeToFile('./output.md', interaction.outputs);
        break;
    } else if (['failed', 'cancelled'].includes(interaction.status)) {
        console.log(`Failed with status: ${interaction.status}`);
        break;
    }

    await sleep(10000);  // Sleep for 10 seconds
}
