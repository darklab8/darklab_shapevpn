export function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
}

export function is_task_id(task_id) {
    return typeof (task_id) === 'string' && task_id.includes("-")
}


export function json_loads(data) {
    return JSON.parse(data)
}

export function json_dumps(data) {
    return JSON.stringify(data)
}

// eslint-disable-next-line
const ValidIpAddressRegex = String.raw`^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$`;
// eslint-disable-next-line
const ValidHostnameRegex = String.raw`^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$`;

// const AnotherRegexForDomains=String.raw`(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]`
const regex_to_match_ips = new RegExp(`${ValidIpAddressRegex}|${ValidHostnameRegex}`);
export function is_ip_address(ip_address) {
    if (typeof ip_address !== 'string' && !(ip_address instanceof String))
        return false

    return regex_to_match_ips.test(ip_address)
}

// eslint-disable-next-line
const ValidLinuxUserRegex= String.raw`^[a-z_]([a-z0-9_-]{0,31}|[a-z0-9_-]{0,30}\$)$`
const regex_to_match_logins = new RegExp(ValidLinuxUserRegex);
export function is_correct_linux_login(login) {
    if (typeof login !== 'string' && !(login instanceof String))
        return false

    return regex_to_match_logins.test(login)
}


export function is_valid_password(password) {
    if (typeof password !== 'string' && !(password instanceof String))
        return false

    // return regex_to_match_logins.test(login)
}


export const allowed_symbols = `abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-_!@#`;
export function is_input_having_only_allowed_symbols(data) {
    if (typeof data !== 'string' && !(data instanceof String))
        return false

    if (data === "") return false

    for (var i = 0; i < data.length; i++) {
        if (!allowed_symbols.includes(data[i]))
            return false;
        }    

    return true
}