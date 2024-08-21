import { MongoClient } from "mongodb";

const uri = process.env.MONGODB_URI as string;
const client = new MongoClient(uri, {
	useNewUrlParser: true,
	useUnifiedTopology: true,
});

export async function connectToDatabase() {
	if (!client.isConnected()) {
		await client.connect();
	}
	const db = client.db(process.env.MONGODB_DB);
	return { db, client };
}
