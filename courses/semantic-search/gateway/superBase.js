import superbase from "@supabase/supabase-js";

let superbaseClient = null;

export function CreateClient() {
    const supabaseUrl = process.env.SUPABASE_URL
    const supabaseServiceRoleKey = process.env.SUPABASE_SERVICE_ROLE_KEY

    superbaseClient = superbase.createClient(supabaseUrl, supabaseServiceRoleKey, {
        auth: { persistSession: false },
      })
}

export async function Insert(input, embedding) {
    const response = await superbaseClient.from("documents").insert({
        content: input,
        embedding,
      })
    
    if (response.error !== null) {
        console.log(response.error.message)
    }
    
    return response
}

export async function Rpc(embedding) {
    const response = await superbaseClient
      .rpc("match_documents", {
        query_embedding: embedding,
        match_threshold: 0.8,
      })
      .select("content")
      .limit(5);

    return response
}
