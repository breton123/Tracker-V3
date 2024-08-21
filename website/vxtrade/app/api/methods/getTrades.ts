import axios from "axios";

export async function getTrades(user: string, account: number, magic: number) {
	try {
		const response = await axios.post("http://localhost:8000/getTrades", {
			user: user,
			account: account,
			magic: magic,
		});
		console.log(response);
		return response;
	} catch (error) {
		console.error("Error fetching trades:", error);
		return []; // Return an empty array or handle the error as needed
	}
}
