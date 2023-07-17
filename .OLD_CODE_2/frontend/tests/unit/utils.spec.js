import * as Utils from '@/util.js';

describe.only('test regex to match ip', () => {


    it.only('test regex to match ip', async () => {
        expect(Utils.is_ip_address("")).toBe(false)
        expect(Utils.is_ip_address(null)).toBe(false)
        expect(Utils.is_ip_address(undefined)).toBe(false)
        expect(Utils.is_ip_address("195.76.34.12")).toBe(true)
        expect(Utils.is_ip_address("mydomain.com")).toBe(true)
        expect(Utils.is_ip_address("my-domain.com")).toBe(true)
        expect(Utils.is_ip_address("my-domain-453.com")).toBe(true)
        expect(Utils.is_ip_address("a b c")).toBe(false)
    });

});


describe.only('test regex to match linux logins', () => {


    it.only('test regex to match ip', async () => {
        expect(Utils.is_correct_linux_login("")).toBe(false)
        expect(Utils.is_correct_linux_login(null)).toBe(false)
        expect(Utils.is_correct_linux_login(undefined)).toBe(false)
        expect(Utils.is_correct_linux_login("195.76.34.12")).toBe(false)
        expect(Utils.is_correct_linux_login("root")).toBe(true)
        expect(Utils.is_correct_linux_login("user46")).toBe(true)
        expect(Utils.is_correct_linux_login("user abc")).toBe(false)
    });

});

describe.only('test regex to match linux logins', () => {


    it.only('test regex to match passwords', async () => {
        expect(Utils.is_input_having_only_allowed_symbols("")).toBe(false)
        expect(Utils.is_input_having_only_allowed_symbols(null)).toBe(false)
        expect(Utils.is_input_having_only_allowed_symbols(undefined)).toBe(false)
        expect(Utils.is_input_having_only_allowed_symbols("195.76.34.12")).toBe(true)
        expect(Utils.is_input_having_only_allowed_symbols("root")).toBe(true)
        expect(Utils.is_input_having_only_allowed_symbols("user46")).toBe(true)
        expect(Utils.is_input_having_only_allowed_symbols("user abc")).toBe(false)
    });

});
