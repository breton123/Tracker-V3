import axios from "axios";

export async function addAccount(
	name: string,
	login: string,
	password: string,
	server: string,
	deposit: string,
	terminalFilePath: string,
	user: string
) {
	try {
		const response = await axios.post(
			"http://localhost:8000/createAccount",
			{
				login: Number(login),
				password: password,
				server: server,
				deposit: Number(deposit),
				user: user,
				name: name,
				terminalFilePath: terminalFilePath,
			}
		);
		console.log(response);
		return response;
	} catch (error) {
		console.error("Error adding account:", error);
		return []; // Return an empty array or handle the error as needed
	}
}

export default addAccount;
