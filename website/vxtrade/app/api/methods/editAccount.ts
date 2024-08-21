import axios from "axios";

export async function updateAccount(
	name: string,
	login: string,
	password: string,
	server: string,
	deposit: string,
	terminalFilePath: string,
	toggleChecked: boolean,
	user: string
) {
	try {
		const response = await axios.put(
			"http://localhost:8000/updateAccount",
			{
				name: name,
				login: Number(login),
				password: password,
				server: server,
				deposit: Number(deposit),
				terminalFilePath: terminalFilePath,
				enabled: toggleChecked,
				user: user,
			}
		);
		console.log(response);
		return response;
	} catch (error) {
		console.error("Error updating account:", error);
		return []; // Return an empty array or handle the error as needed
	}
}

export default updateAccount;
