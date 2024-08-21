import axios from "axios";

export async function getSets(user: string, account: number) {
	try {
		console.log(user, account);
		const response = await axios.post("http://localhost:8000/getSets", {
			user: user,
			account: account,
		});
		return response;
	} catch (error) {
		console.error("Error fetching accounts:", error);
		return []; // Return an empty array or handle the error as needed
	}
}
