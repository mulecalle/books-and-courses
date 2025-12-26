import fs from 'fs/promises';
import path from 'path';

export async function writeToFile(filePath, content) {
    try {
        // Ensure the directory exists
        const dir = path.dirname(filePath);
        await fs.mkdir(dir, { recursive: true });
        
        // Write the file
        for (let i = 0; i < content.length; i++) {
            await fs.appendFile(filePath, content[i].text);
        }
        console.log(`File written successfully to: ${filePath}`);
        return true;
    } catch (error) {
        console.error('Error writing file:', error);
        throw error;
    }
}

export async function readFromFile(filePath) {
    try {
        // Read the file
        const content = await fs.readFile(filePath, 'utf-8');
        console.log(`File read successfully from: ${filePath}`);
        return content;
    } catch (error) {
        console.error('Error reading file:', error);
        throw error;
    }
}
