from .ansible.create_hosts_file import create_hosts_file
from os.path import exists
import subprocess
from pathlib import Path
from .interface import ui


def test_host_creation() -> None:
    create_hosts_file(
        query=ui.UserInput(
            ip="localhost",
            users_amount=5,
            user="root",
            auth_type=ui.AuthType.ssh,
            password="",
            server_ssh_port=22,
            server_vpn_port=31299,
        )
    )

    assert exists("hosts.yml")
    assert exists("hosts2.yml")


def test_capture_shell_output() -> None:
    result = subprocess.check_output(["echo", "123"])
    print(result)

    assert result.decode("utf-8") == "123\n"


def test_capture_shell_output_and_get_status() -> None:
    result = subprocess.run(["echo", "123"], stdout=subprocess.PIPE)

    assert result.returncode == 0
    assert result.stdout.decode("utf-8") == "123\n"


def test_capture_error_output() -> None:
    result = subprocess.run(
        ["cat", "e5t4lkt54j.txt"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    print(result)
    assert result.returncode != 0
    assert (
        result.stderr.decode("utf-8")
        == "cat: e5t4lkt54j.txt: No such file or directory\n"
    )


def test_lack_of_error() -> None:
    result = subprocess.run(
        ["echo", "123"], stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )

    print(result)

    assert result.stderr == b""


def test_capture_error_to_stdout() -> None:
    result = subprocess.run(
        ["cat", "e5t4lkt54j.txt"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )

    print(result)
    assert result.returncode != 0
    assert (
        result.stdout.decode("utf-8")
        == "cat: e5t4lkt54j.txt: No such file or directory\n"
    )


def test_capturing_non_zero_exit() -> None:
    result = subprocess.run(
        f"mkdir 1/2/3/4/5/6",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
    )

    print(result)
    assert result.returncode != 0


class Result:
    def __init__(self, stdout: str, returncode: int):
        self.stdout = stdout
        self.returncode = returncode


def test_capturing_doubled_output() -> None:
    log_records = []
    proc = subprocess.Popen(
        f"echo 123; sleep 2; echo 456; sleep 2; echo 789",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
    )

    assert proc.stdout is not None

    for line in proc.stdout:
        line_str = line.decode("utf-8")
        print(line)
        log_records.append(line_str)
    proc.wait()

    result = Result(stdout="".join(log_records), returncode=proc.returncode)

    assert result.returncode == 0


def test_capturing_stdout_and_var() -> None:
    result = subprocess.run(
        f"echo 123",
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        shell=True,
    )

    print(result)
    assert result.returncode == 0


from jinja2 import Template


def test_rendering_stuff() -> None:
    with open(
        str(Path(__file__).parent / "ansible" / "files" / "hosts.yml.jinja2"), "r"
    ) as file_:
        template_content = file_.read()

    t = Template(template_content)
    rendered = t.render(
        is_docker_py=True,
        server_target="wireguard-pass.light-search.com",
        users=5,
        user="root",
        password="test_password_for_pipline_usage",
    )

    with open("hosts.test.yml", "w") as file_:
        file_.write(rendered)


def test_encrypt_something() -> None:
    from .storage.encryptor import SymmetricEncryptor

    private_key = r"-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQCmn8+4Wwm1k2cl\nfBcAUIoIX2uGluvdIIUr7vQA4cnRJ2EkQ4mGN81eaW16o4OS2ExV7aX3ymWpc8rk\nggjItM7/mKePlZ9C8j5iKVkSQR4x513OWRKqtduFM6iZjIsQoPAU6dAM8c1OS129\ngsGeW/9IBFWr0gMd7Aor47qUWSvywoU5qyFVf2a1iMhiSW8c24L8Iwle5V0Rmc6V\nZ40nG6TTiZqkBvWF90QUgP/AbYiuTep96/dXDyTRlpcfuwuuEPqW9M81BJm5pgnF\nQoqW1AR9jsVhDE6Dv910L6uvUKYJxeGgbVPw6IrRWZvmDCbh/116JtOgEawnLaU+\n1u+uGct3AgMBAAECggEANGzb4llieKrkLTsZ0ZOFmpTLNBGQLIbq36PTSePAp/oH\n6m0FfCFakHYDaC7CWxWLDw4yxf/8dJBmKfdv5BZferQBJIAjF+E4F5KC3+d1JKZz\nMVV9NhD5/LMAPS+nIZhBcZMPTsNVoWi9Gb9mQ/kWHQagHet555Q4rw57yek0lrBz\nHsUlzpkxrsTMjgy50O3U7em5o5dukvCxoKIhrBcR4P7IDuGaKoZjWSDER8F05/Ra\nQwtXtnf/86F8slRsLEnO71e1O6f/lNFMWhJOsCngzD+dp8GJzBbLDp/kTqSNYNYV\nv9pP2S5+K8Wsd7R+vsAPGVmnF6YeWmfGNHg7OUQW4QKBgQDbXs0ipyBVQ9HUCf3+\nuczFSlIkYe7BZnyc1//txY1aNQ4Qt4lsY4YPei3RY939EyKo3rMJ5SDrMv2S3P8O\nTcBvHEmQmRgyi5TFRtBx5hgHGJIu5IRt9PSeQ9GiRS2ZU8tiAK7/siBGXoK8gAfy\nr8DtfiyP+fUPdMJQrAD4ecHuJQKBgQDCclQUlacfQBKvlFF/z5H4fu4/2b2e3e0E\nO/4Qun0VoWeDMvAjoHlG4kgW3ZtbOCFYrAPOYn1dxud56KLhTyg66l9OdWvXZxEa\no095P9lTxwLrtjJXrFWpS75KyTnkqs/CJSGBPnSMOsZIdoqawS6F6q+341QCJZry\nfbMoTNWaawKBgE4a9OLPqn1xRjY+0IZvVO8xxQlbLQ0DFn8pkN/xpKBnn3hoQK+s\nx8Ce+c1Bx3oh5AdIM2rkf9H+N7agpNdM66Uj5zVqrOjiNbf/vJuxFwD/yJyVlGkp\n/CaVcwBZrSCYayObprM3krI7WEUROMM5vHFSqT8h+hTkt4LNmxLdFyVZAoGBAJs2\nGYmI36shQQkoMln8fX9HCrSrASKD8YLUxHvj8J7IhNEEYw19NfFwBK1D3ZPV3UBj\npnIiygGGGRWFriZ9QhatKMB/GEMLwWpq+7BEWBz4mYs/lzXGmWYW0OHveCfgdRB7\nBSCekvewnsAO55qaI6G/8N2vN0qza9iun8jGdCbbAoGAX4FZ+q4P3hzJhjKf/0JX\nVTaIW4TtIDmar02H0n8a+z1Ol4qOqEr53TtG5lNwjL49ZV+07csC4KvdWTrVIcfg\n+et0jJu3g87JRDD1/rHXWGViaVCV3O7Nc1TK921ENV/cc3ow/bJ/9c/U9dKiHUe2\nkxMgQs/uB8PBfxZJb6VTFNU=\n-----END PRIVATE KEY-----\n"
    data = r'{"1.conf": "W0ludGVyZmFjZV0KQWRkcmVzcyA9IDEwLjEzLjEzLjIKUHJpdmF0ZUtleSA9IHdQZUs4Y0xIQUJrZEpJb1EzUzlna1pCTTZ5d1ZBWVhZTnNRbHVQK05IbGs9Ckxpc3RlblBvcnQgPSA1MTgyMApETlMgPSAxMC4xMy4xMy4xCgpbUGVlcl0KUHVibGljS2V5ID0gQ1E0RkRsL0dkMjdXcDlHelFpUUFrZkNKTGduWmZHVlZmcktFRTJidFNqZz0KRW5kcG9pbnQgPSB3aXJlZ3VhcmQtc3NoLmxpZ2h0LXNlYXJjaC5jb206MzEyODkKQWxsb3dlZElQcyA9IDAuMC4wLjAvMAo=", "1.png": "iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQMAAAAFsTfpAAAABlBMVEUAAAD///+l2Z/dAAAAAnRSTlP//8i138cAAAAJcEhZcwAACxIAAAsSAdLdfvwAAAOISURBVFiF7ZdBbqQwEEULsWAHF0DiGux8peYC0FyguZJ3vgaSLwA7LyxqnruTmcwiI3VlO4hEdF4rNlW/fpVFv7vkP/knOUQm3buUb2PfpfgQ6bxUVnJqXnhM8ZB8a4a70y3wRyvx/cRjYrX69Hp3fRd4tpObRA3DpnFLsvi4/ZA0erlh8yIjwfgZIQbaVz4vIXchT35fvkTnXVLyE/q/7i+Ze5eUK+jVEMiyIG+wfVHVu6Qk2Q3XuIvI7HKl8XKvGFjI6es18N77lPbWxbsgn2G1kqPpl1RvflC/34TfMkuurORyegaZm751e+Xjmvhu3KzkGHOXyt/ukjtfgnFzhNZILiGEJKeXsehIXHw0r4haCD+TZzW9NxnhVCG3ZN5KLqlR8cauRxGXW0cwxExOjEpzp7hUPMPOIhT0ZickZCe9W6ovSrkU8SuiNiIdJRvQI54nxKAKulnJITgo9VFfsi+sgB6bwUzOtE++RoyI+mriqqi7Xq0E7WyFsPF+UqokHoTBSigytklcL0otkCVKsK/MhMujFzyg9LF27KcU1UoOHhWjGg76WNn1n/xYCPHzSp3NblDN7fhMlJWgnSpQFjUdW0bqb+C7m5Uc7Lehx+7S5LkhS7Fo00ouoeHogy0/zWAeEbidaBowv0opuCySF1yQuFoJ3UYwZq2fg0/flkY0bFZyluRQZ9Tx8HB5lmENr3VMJBDL8u/pZp3Pk1IlH05hIjho39F5CKeLF++BPZtJcZThIdzFse6CiOJqJTiKBnZKnikX1Mgb1KeZuDylfglF1x3rjPFM9WYlx4hX9TM9h5FzRDi03L2ykmsU6pVPSxkBuFn2YwcGounZK5RWRn52cdI2Lz+wkLOUBbpmdAXS01BiP5lJmUqUcQwHJe33kV2LmVyOgY5dkx+MgZzLPH5W8PuEnWIwuFSJpcbVFxmeVoLHI5w19TfHroskbx/dzEYYdmpGzinpSlyZpNyrSiwEP+h8fZSOURz60fAGg5nw6T4OjIp4TBUKqdKgVkIHY2gtEfUlM2XXH/3HRsrIg7soc5OiSszgc533Cda+BJwvs2syswR0XZsJMzWDGB0DH+Xw+hxpP2dYA8FaRm7Gfxo4acf8ZPkBYQTbEqc6Wgd9cn8d6cyEViYNOSknuS5xCFA1Ey1n3+d5mlRTK6z2+4T8NiE/fGqLm+7PLJWCXqzku+s/+Rf5BU3kFzIcvLb5AAAAAElFTkSuQmCC", "4.png": "iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQMAAAAFsTfpAAAABlBMVEUAAAD///+l2Z/dAAAAAnRSTlP//8i138cAAAAJcEhZcwAACxIAAAsSAdLdfvwAAAOXSURBVFiF7ZhNjqQ8DIaNWLArLoCUa2SXK1EX4OcCcKXsuAZSLgA7FgjPE6p65vsWPVK5t4NQtYpHqgT79WunRb+75B/5K9lEnrp2fhXf1EeaqrWOUljJrmcfpdY0ydlWbow6Lzy0ktg8Fx0P6bXcow6hqRdWtpNWSl3crGmGxzT/lOgV3BxF/EoYfkT07KQp4tkvZ72cz7j2f6LzMcn5WZr/3f/J3KeE66q4CeTZa9NWOv9R1cdkI8nEAO2IdOEsNA3hFQML2aPbgvTL+jzWR0iDuFF1tJKtEgnlHJ3GtRU+EdFZWMkVdPJrVzWPsBYxjQfxSLOVbNXJfnk2yFlHRzDaQGiNhF/dF5LTiM86kkARvyJqIYSzjrofaWDBpSmW81G52Uo0lqh48mnwhJbHZAl7MJIrrLWerU+bsH1qrkRNduIJ6ipV0qPMAs9FfD6tZFepl7z3ccHzRCoplleVWMgljiK+Fb32B5664qZmsrPHyNsLoibzo6LucrYS1pkzURT0VKokbYTBShQf9YmEX3IWC32j6Y+mMBN1U9YLNoAk5eFxvqRWsvmmp0SIa8Dz2HW2rtlMJPdD6qwLpOV8eBQkvZWgHRaZtZz46+UZ3fCVOQNhnf3gvZH22VVkKWVtWgm94vZjp7cZdL5ER2aieLxHgLz6KXL2uKC+dG0heJUENuvuwad55EbU1FaCDQwVdYaVuinc6xzvHRjIJsQSLVO+TGEMUGv7rhIbSZNvOsJAOEO6e/i7z1lIdbedSid0tJQDHUPSbiV7NgMM/szVduRwIm0z2QIezOiUdV3HcsAbDjuhj82x6e6eNvg1TyiyFlZyeemoNiw5jwDctPG3jxpI1k5uaESC/KwShPbYW8mey4IwMLpmb54PN2Z7tpLsmghnJT891uLZtZjJxTZ9ur0Kj8EPpPXvPmcgCEcPZjHNsWTBmGW4Wwm67tWNR9MGdk0rY+p5e6KFcIbIxxFmWEZXdKRTeGnHQphxnrHc7i5BQ0+Mn1KOVsK3wbsr4Fi4ssMbGJDVSjRPmlhU2qN03k3CTPH2eBPJdkXZcWYqNJ/AdnW7lWDt/X1UelQMF8QVVX69z+ckn+cCIaSJoZ3ykvKrN5pIthZcmfGfCbHkXMJV/ICgmvlQXWgd9Mn1daQzk1YY/PGnRP3Vhw7Ve7q1EEb1gHzIDAMjtcJqv0/IHxPy0wrWgq5zb+TxxahoJd//3+Uf+Z78AtyGBX3vG3kyAAAAAElFTkSuQmCC", "2.conf": "W0ludGVyZmFjZV0KQWRkcmVzcyA9IDEwLjEzLjEzLjMKUHJpdmF0ZUtleSA9IDJNSmxJQkJOdTg0MlAwQzZkOUpXMDYyb01veFlwd0dBU0hPeklqWmxqWFk9Ckxpc3RlblBvcnQgPSA1MTgyMApETlMgPSAxMC4xMy4xMy4xCgpbUGVlcl0KUHVibGljS2V5ID0gQ1E0RkRsL0dkMjdXcDlHelFpUUFrZkNKTGduWmZHVlZmcktFRTJidFNqZz0KRW5kcG9pbnQgPSB3aXJlZ3VhcmQtc3NoLmxpZ2h0LXNlYXJjaC5jb206MzEyODkKQWxsb3dlZElQcyA9IDAuMC4wLjAvMAo=", "5.conf": "W0ludGVyZmFjZV0KQWRkcmVzcyA9IDEwLjEzLjEzLjYKUHJpdmF0ZUtleSA9IGNPQ29YUEFacnlzT3VrZFlDYWUxU04wQjN3RGtRTVBDY3haVThVRUJ3bVU9Ckxpc3RlblBvcnQgPSA1MTgyMApETlMgPSAxMC4xMy4xMy4xCgpbUGVlcl0KUHVibGljS2V5ID0gQ1E0RkRsL0dkMjdXcDlHelFpUUFrZkNKTGduWmZHVlZmcktFRTJidFNqZz0KRW5kcG9pbnQgPSB3aXJlZ3VhcmQtc3NoLmxpZ2h0LXNlYXJjaC5jb206MzEyODkKQWxsb3dlZElQcyA9IDAuMC4wLjAvMAo=", "3.png": "iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQMAAAAFsTfpAAAABlBMVEUAAAD///+l2Z/dAAAAAnRSTlP//8i138cAAAAJcEhZcwAACxIAAAsSAdLdfvwAAAORSURBVFiF7ZdNjqMwEIULsfAOLoDka3jnK4ULYHIBuJJ3voYlXwB2XljUvErSPT2LbinV20FICXxRbOrnvYL4u4P+kx/JQTTjSy2rm8ZaNkNjpE5LTm4hApaL2s3Y1dk94aaWxGlOWCiP3J+RVz+NSVZWk5spnOzOZa8UYtl/Sche3u6RyGWE4VdEYtC62EJqY2pzzOFrdN4kkp80/XN+ydy7BMeFXRsEsgVGPHj/W1VvkwNJ9vZymYgW3zouq3/GQEPOWDhSSHmuefBlJbt6e9eSw+Q5lT1ajhmJwq8WM3Vacnk+k1wNPnex3Ctvpuxacri2kNxbqY1RgnHzCK2SXFSYkZyJnNQReTRxf6qJoS4iro1MQ+F0qQ3G7lpykPzrRrw6It8GbzdPo5bgoUc0SoW6lDPlUVowqwlXSTh6bqz9ZZAuNPEzohpyVhqhVannxFACMuWeeFeTJE28eOw6B6yAejSviteQirruUYyiWFiEUd09awlHiDoIFpxmRpeUw70iqiIwinKKxrQulY2mUJ89pyJsV9NvogHiY4PDaoW15HDUVeiUPTzSgl1Dm3lXEyqbszDYxVvmNjhUEAUtORmLiDFu+HQ0R4u+2bXkwH6d2A46eDHIEqL70Y3vk4tgONK4/BCDxfX3pCeoHZj/nfHojQitnDuegpogBhBmto/BZxrEiJ4x0BD4zyWmASmFSmEdCOGzdjSEE2I5kZ/gZqPUeLt9dImCnNA8Ny2uSThFFdDHrdMSTmI7mxFhPlO/Qpip3LXkcBjEMHK2R7chnAhqryaXb0hLSFLXY+xXV86qJ6eMcnh63IYFZZlQYLxacjmRZFwFGQFwtrk+a0dDuCKKSC+sDKtl8jSYHLTkrGgOdC32Dsh7tXeRZy1BXRN1KSM/IWL2x65JTS4/DaY9tEqEYXF0c5a1BDvFIACVklhyuUcpw1NL4F1irXW6eewaVoaR9qWJGmKQIhk55wrFwvgpPd1pCWacEDFAiVdDoTczLZ/zwftErhBC9C4GYciVw5eXNyqIOJhvN0k7LbA1V/DbXU/EHjmiiSFR0nNQaNYSSHtIyAxG10kUNKKuezXBTL14yAkmO9ROf8lI+/lW/T6JkGScGDzRKz3eS3CEXxBUzV6f1mEfhfmaOnUEnkMG+lQuVHTl1TCrCSPVkAGM1XixRq9gtc835LfJ4z243xyeW7wRtzFlBC357vhPfiJ/AAPGHWgYJCJnAAAAAElFTkSuQmCC", "3.conf": "W0ludGVyZmFjZV0KQWRkcmVzcyA9IDEwLjEzLjEzLjQKUHJpdmF0ZUtleSA9IFlEZlVBRjdoUno2aWt2ejVRSktudVBrNWpGa1ZCbUh1dkxsamtRZk9XR289Ckxpc3RlblBvcnQgPSA1MTgyMApETlMgPSAxMC4xMy4xMy4xCgpbUGVlcl0KUHVibGljS2V5ID0gQ1E0RkRsL0dkMjdXcDlHelFpUUFrZkNKTGduWmZHVlZmcktFRTJidFNqZz0KRW5kcG9pbnQgPSB3aXJlZ3VhcmQtc3NoLmxpZ2h0LXNlYXJjaC5jb206MzEyODkKQWxsb3dlZElQcyA9IDAuMC4wLjAvMAo=", "5.png": "iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQMAAAAFsTfpAAAABlBMVEUAAAD///+l2Z/dAAAAAnRSTlP//8i138cAAAAJcEhZcwAACxIAAAsSAdLdfvwAAAOOSURBVFiF7ZjNjeQ4DIVp6KCbnYAApaGbUionYJcTsFPSTWkIUAL2TQfB3Meqrp3ZQy/QnOsUCv2jr9CSycdHqom/e9Ff8r/kJJq5r4mfwU2t7lSmRIOWXLJMWDupP6x/Bn9kLGpJcjN+bGVgc2G36KaMnfXkYStnf3A9Gq2pHn9IiO/oj0QUCo7/R4T7Et2Q+pr7lPucyvorOj8mkp/s/vP+LXM/Ja+Xvy0C2VdGPPj4XVU/JEgy8nOHQkRL7APXM75joCFXqvi25jK3Msb6JMiHNy05bZ+Q5+Q5lQfhK82tD1pyR8iQFuvGWIZUt8a3rYeWIAYLydqT+pQ8gvGICK2S3BEhRHIcBdERxbpbN6tJoCFhN35aJMoNuY/IvJac1kDFe6jPQBQh7bpHPbljmbjPDTGoVy4j0QPB0BI4ymkLWdSuue3rg01PbqIpix5heHACCn3IfKhJkCJeovjx2uCpBW6qJleDAeDp8eio47ox1G3UhBM8D4Qv+AqjSuoJ/9MTOSYSfhOeHmd3a3ODmrDhzHv0GxP62BhgV4a15AxiLUT+jEgLTt3f5qckBGtxo0WKPHMfg0H+Vy25GMWBEJodRhpoTv78ZE5BTjkveiyk3ReLLFV8dtKSO7pH6COO/DKDJZgt6wk3/x4BbtuJ+tqKKEhLTjEV8ZjX4ONGaURfvqMgokErf/vIfocfN0f07o0aIqZu3SMSzjuJcPojfPxAQajeAZVRN4QzVrEr+/EqBQnSdnYrNn9l87Qou7ppCUMsGVt1CvADqBFB/apGBbkjDN6tWXQ9JfMM9Wp6cgb4MZ4eyxiKISK0jjJoCXrjyh6/rTIC4I1tzaEl3HBSlAUigd0KRRptWbVESiTBR3F28eaj+S2/pwAVwdzEqNoCB10TBjGcmtTklp7vXl6FRgQ/oCV41hIIB/KBnCWWXLckMry0BH4wZxoayg6nRitDzZVJTaw5kkFPmxtGV/i9aHPQEsw4azKn9Rg/4dAY6xYiNRGPD+j/8D+4Moh/xi8fVRDpYBFjrL+SZGa3v2YKFZH2uBO6Nx5dJrKLvZrA2le5JzmCm8LgMbNnoyav+xzsxKDmZnQhMp/eqCLJLQFyRuURdsC9hD6Z0xFU2NFgqGjdyFX5TChagmsE9Mj1hv81XAK++pyGyKjuXvdpDIyoFez27w35x0TatQx0cFPpjVi+MSpqyff/d/lLvif/AJ1+B8PlCUkAAAAAAElFTkSuQmCC", "2.png": "iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQMAAAAFsTfpAAAABlBMVEUAAAD///+l2Z/dAAAAAnRSTlP//8i138cAAAAJcEhZcwAACxIAAAsSAdLdfvwAAAOWSURBVFiF7ZfLjeM6EEXL0II7KQECTIM7piQlIFkJSClxxzQIMAFpxwWherf8mZ63mAFc3o7R3bB5jCZVn3uLxH960T/yV3IQLcxXKHdvh1o2Q0Okm5ac3EZTLsNHKBzbxN2esKgl0c6hWyNvPpPvLqIh0fQFGU3Hye1c9kpLLPt3ZIl2SOWMNDD2cV8RxnMjqOUwbQ6AbfmJzscE+ZmS/d/PT+Y+JiyptgPnKbXR88rd+VNVH5ODLIXubniPkpklNvJl15IzurXmJeWp5h71SO4uuynJ5fHv8+wLPnFqvcc+3a4lZ3UXyae1dod3jA2j9I2OHNSWmm8R521DdJfPY2hfEN5w9pBng7O7M7nDk5qcnEc8dMrY5B7yUgv6j7Xk8lIse+W7JwqIaNmklJSEK8LpDnJXaDN1EBjkfNWSk93KtjcFR0YH3w3O7vQkoXZ4T4XlL7qtW9MrOiqCesEyTg0pdZu3/Ts/CoJf8ogoeBvYMZKTspqcEM7YndAn6IqQcvg8qAlLDZLp7qFs8CLUeHr1nIIcvkD8RiJUzeXbQ+9p0JN2QxjIHYF3OXUb5Y2SIC1XQEIa6OgloqidU02kOWA+9hZpikgRvvHMtoagPw4Pl0BQ22yQJbTIKwYaEpBku2Ah2R7GGHlNzy5REXLwWJgt/GeqdBNjtIOWYJkCDtuJSaKVMVlgNy1BIXNE12bZpGKNZvOcAjTkkFRD41E7nXhRLYwK0pIT05zHAIWIYqYoF/Jv2k1L0K8z3lZRvpkyuuR4+4+CXAFvYY/i/DA0mfLwEHqCJKN2uk0mxO7uy1lfjq4gUCno+o7CYdH4w4ig6oks5BmSbKAxotBw3UVLuGKaQADKKfnJFKg3XxBIO+zRuLPCG+1MBd9lLcHUDxNbqsxfG6QU94CX06oIjhmQEOQHGtNm/9A/LeGK0obgdRLL53J8R0dBEmoZU2eHr2zebea36HxO4D9iYhF6gDDAJ1E4zxhoyJky0ntLuM9hN3Qb5sTXfK0g0NE1YprDpVCudLim9OaX+n9MGD4W2vjQZkydO7yR7BfkMUBF0aoet0Pj3v6jITIChDxJtmGPloy9JT3BQ0Of9oqRRy7BF2Gk/XU7/JzAxzARy42Tesq4l0g8viAjQQzyKDvgxg9HsssXZILAG7Qdehf+AyF8zbAawqLKk/g2kcEIYGf/1sTPycOuIaKYU8QbsTyl15SmIH96/SN/I/8Bt3g4XIk2IbsAAAAASUVORK5CYII=", "4.conf": "W0ludGVyZmFjZV0KQWRkcmVzcyA9IDEwLjEzLjEzLjUKUHJpdmF0ZUtleSA9IFFESTBsdk8rQkt6czI5eHRlZXVLMjhwdFNOMS9tR21BeW1Sc2h4THVXRUE9Ckxpc3RlblBvcnQgPSA1MTgyMApETlMgPSAxMC4xMy4xMy4xCgpbUGVlcl0KUHVibGljS2V5ID0gQ1E0RkRsL0dkMjdXcDlHelFpUUFrZkNKTGduWmZHVlZmcktFRTJidFNqZz0KRW5kcG9pbnQgPSB3aXJlZ3VhcmQtc3NoLmxpZ2h0LXNlYXJjaC5jb206MzEyODkKQWxsb3dlZElQcyA9IDAuMC4wLjAvMAo=", "zip": "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'

    key = SymmetricEncryptor.generate_key()
    encryptor = SymmetricEncryptor(key)

    encrypted = encryptor.encrypt_str(data)
    decrypted = encryptor.decrypt_str(encrypted)

    assert decrypted == data
