import { GetEmbing } from "./gateway/openAI.js"
import { CreateClient, Insert, Rpc } from "./gateway/superBase.js"
import { sentence } from "@ndaidong/txtgen";

await main()
async function main() {

    CreateClient()

    const query = "A cooperative elephant is a nectarine of the mine.";

    await semarticSearch(query)

}

async function semarticSearch(query) {
    const embedding = await GetEmbing(query)

    const response = await Rpc(embedding)

    console.log(response)
}

async function insertData(entriesToAdd) {


    for (let i = 0; i < entriesToAdd; i++) {

      const input = sentence()

      const embedding = await GetEmbing(input)

      await Insert(input, embedding)
    }

}
