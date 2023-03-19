// initial guide: https://www.robinwieruch.de/axios-jest/

import * as Requests from '@/api.js';
import { API } from '@/settings.js'
import * as Utils from '@/util.js';

describe.only('testingRequests', () => {
  it.only('fetches successfully data from an API', async () => {
    // arrange
    let data = { message: "ping" }

    // act
    let response = await Requests.PingGet()

    // assert
    expect(response.status).toEqual(200);
    expect(response.data).toEqual(data);
    expect(response.config.url).toEqual(`${API}/ping/`)

    response = await Requests.PingPost()

    expect(response.status).toEqual(200);
    expect(response.data).toEqual(data);
    expect(response.config.url).toEqual(`${API}/ping/`)
  });

  it.only('fetches erroneously data from an API', async () => {

    await expect(Requests.Wrong()).rejects.toThrow("Request failed with status code 404");

  });

  it.only('tries to sleep', async () => {
    await Utils.sleep(500);
  });

  it('Check status', async () => {
    var status = (await Requests.Status("15610bbc-2e26-442d-8566-78cbf84de9de")).data.task_id
    expect(status).toEqual(Requests.STATUS_STATES.success);
  });

  it.only('Checks_if_task_Id', async () => {
    let task_id = "15610bbc-2e26-442d-8566-78cbf84de9de"

    expect(Utils.is_task_id(task_id)).toBe(true)
    expect(Utils.is_task_id(null)).toBe(false)
    expect(Utils.is_task_id(undefined)).toBe(false)
    expect(Utils.is_task_id("null")).toBe(false)
    expect(Utils.is_task_id("undefined")).toBe(false)
    expect(Utils.is_task_id("54kt45t4j5tlkj45ltkj4")).toBe(false)
  });

  it.only('Parses received config from backend', async () => {

    let data = '{\"3.conf\": \"W0ludGVyZmFjZV0KQWRkcmVzcyA9IDEwLjAuMC40LzMyClByaXZhdGVLZXkgPSArTFJUM0FodmtObzcwdlZPZnZaVmFBSGcveUhobXV5Z09TUENaa0N2ckhzPQoKRE5TID0gMS4xLjEuMQoKW1BlZXJdClB1YmxpY0tleSA9IEZCWlFFdUlJZVU0RUVjWFhTOWF4clZWVERvMDNjN2J1UVNWYVB5RzYwd1U9CgpFbmRwb2ludCA9IHdpcmVndWFyZC1zc2gubGlnaHQtc2VhcmNoLmNvbTozODkKQWxsb3dlZElQcyA9IDAuMC4wLjAvMCwgOjovMA==\", \"1.conf\": \"W0ludGVyZmFjZV0KQWRkcmVzcyA9IDEwLjAuMC4yLzMyClByaXZhdGVLZXkgPSBpUE16YkFwRzkwNmpxMnoxRTRyck05YTZ1bVpCVzdYTEE3R1ZGY1VyWmx3PQoKRE5TID0gMS4xLjEuMQoKW1BlZXJdClB1YmxpY0tleSA9IEZCWlFFdUlJZVU0RUVjWFhTOWF4clZWVERvMDNjN2J1UVNWYVB5RzYwd1U9CgpFbmRwb2ludCA9IHdpcmVndWFyZC1zc2gubGlnaHQtc2VhcmNoLmNvbTozODkKQWxsb3dlZElQcyA9IDAuMC4wLjAvMCwgOjovMA==\", \"2.conf\": \"W0ludGVyZmFjZV0KQWRkcmVzcyA9IDEwLjAuMC4zLzMyClByaXZhdGVLZXkgPSBVTkZDZTNQWm95aitqeEFQWGJoT3VTdXZNZXhaa2ZjWm5JdERqdkIvQ25VPQoKRE5TID0gMS4xLjEuMQoKW1BlZXJdClB1YmxpY0tleSA9IEZCWlFFdUlJZVU0RUVjWFhTOWF4clZWVERvMDNjN2J1UVNWYVB5RzYwd1U9CgpFbmRwb2ludCA9IHdpcmVndWFyZC1zc2gubGlnaHQtc2VhcmNoLmNvbTozODkKQWxsb3dlZElQcyA9IDAuMC4wLjAvMCwgOjovMA==\", \"3.png\": \"iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQMAAAAFsTfpAAAABlBMVEUAAAD///+l2Z/dAAAAAnRSTlP//8i138cAAAAJcEhZcwAACxIAAAsSAdLdfvwAAAOBSURBVFiF7ZhBzqMwDIWNssgOLhCJa2SXK8EFoFwArpRdrhEpF4BdFhGeZ6bzj2YxI/3udiqEaL6qTfLsZ6fEf3vRf/JPchJNgc/g1khdxD0PeNCSi9uczJbkqwd2C5UjYVBLoptCxhfvlBdqE7kh0fwBmZPrYhtkym2ufHxG1mi26rD0NZmDPyPcJmuu5NbUOsan8PC1O98m0Aez/uP6rdy3CV53oJX5Sm2x2F0ZZi05Ay24RBkiD2KOmjs1seNu+ajm5QnzJYtQGi8t4dSGyhxp8m0h3hIEb7Oa1HJa87Ktq1BpfHmzRd605AyZQp78+CLqUp6Cww8OWsIShg3BeHpzRChfLh4PLUEMLqH1lCdZgettXquIryO3NzdlOEEXafEIzHJVs2kJArBDBjPuZQ9mD08268m4h7wEc1s+PeZbjjhuWoJ3k6XFIqpphSskxiJWLeFk7uAGaBLNixx5ovDOYAW5Q+6JZdi33pbdiuVvWsJxPCBvEpt5nA/u8s45DYFrpibb4GF4WRLurY+GnGFEAHbya+UkflmEuTm05LY/bXg8UjlDg1dd9eesNeSqBYVxJ1gLchdjqLTvnFMQ7AGFcmMM9ac2FMaJPiBxPEVes1uo7fqAUqYnUrfJsBRGN7O5ovjfpiUMR495smLPsMAulo31BPWHaNzJSCQid6ES0aAlt8WK4S4oYs9HfNkqX1pyQmdEH4+coHZ5BZF90BLE3RZpwC6mPEc31IZ0YTVhRxDZS0GbHnvu7TuuFYRhdTaTZSz9hsdbxA7NWnJJ5TfQ/ET9l6h0Ur21BPnxkgu1ApyGiI7srZyCIGXR0/WEAIQ9S34wt1VL8G5LkBqlI6MXI+yHN6wlnDIE2eBPKNpehNqt69SEnw1A7xlld+eY0VYcalKp90WMCk4vrpwXn2c1QYMTMYCqiDwu0mj/6tI0pLoFs5YYlMqDwIE3qAkaHHmMkBr3Jl5VW6clV8pdLTuazSrt2G7L0xQoyUnwg9wlcSnJOdndcmkJorhH98oFPWwvhVEs/9ATiejJs7gLPIbk5DRryWPtEs7w0RXniYBI/DpNfZs85zmkGo6/rUerLiswl5rg5FphKpAaAY7eE/CramrImsbbQhaEYXka9s/Ic9BBKkNtHHFkM9SEceSSXgyJ8pIUebJZS+S/DTveBO806MUWNHoxz1qi+UfmP/kB6CCua168lXsAAAAASUVORK5CYII=\", \"5.conf\": \"W0ludGVyZmFjZV0KQWRkcmVzcyA9IDEwLjAuMC42LzMyClByaXZhdGVLZXkgPSBHSzNiNkNucVV4RmNkY0cwakVvYUw3VllNSjk3aFp1bC8xSmNJZEhBVW5vPQoKRE5TID0gMS4xLjEuMQoKW1BlZXJdClB1YmxpY0tleSA9IEZCWlFFdUlJZVU0RUVjWFhTOWF4clZWVERvMDNjN2J1UVNWYVB5RzYwd1U9CgpFbmRwb2ludCA9IHdpcmVndWFyZC1zc2gubGlnaHQtc2VhcmNoLmNvbTozODkKQWxsb3dlZElQcyA9IDAuMC4wLjAvMCwgOjovMA==\", \"5.png\": \"iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQMAAAAFsTfpAAAABlBMVEUAAAD///+l2Z/dAAAAAnRSTlP//8i138cAAAAJcEhZcwAACxIAAAsSAdLdfvwAAAObSURBVFiF7ZhLjqMwEIYLecEuXADJ1/COK8EFIFwgXImdr4HEBWDnhUXN50wyj0WPlOrtRJE6zddKQT3++t2iX73kP/knOUSGdZ9TW8UsXVutuVmlspJT8xDzoP5eu1N31X2JXLSStR07P69+Sftd3NHlJsrwHRLaUXaN29jlWyDOt0jf7VdwusoYiPM9ornv8pByX+ep5CBPv7PzMSn1ie1f7z8q9ynhdXSbdBvVnlLbqD9/d9XH5Ki3Pki1UhypIqS9iZ+tRNVdYWvivqxuWfUeILmxkqOTZt0m3SYuEypReb9Yiap/1DTOzqMfwWsiqW62kiNQkK1JQrWF21d3J7KduDM5Ro1OHFbl81X700ouYebco5Yp5SrtjyC9tJWZ1KRh6xGDWDp6UUqdzUSjSGh7cSeSsLqSkviqj4WoPzrPzQ6KGKgmR/sMVnJGudV6dduQ3EwOuJL200oO8VrEjznWWdsp+SPkwUxC6ZRDUCxpiBD9PbjFSnjoIgCJjnZzZF1kZLWxEqSliZRlG9g8SEtEpF/KZyHoscooMv1UqaJ8uljJJURob51Mqz9LqJawp50wItuta4dEB/FXT5G2ErRKujzSPkWo3JI2Zs5MNPoz0YntWOcGoSoz96q2gZzPnSNoZyyT90AMXspnIQfKtNLL/qhzsQNKOtvJSpg5ETKKxrOFNtJwiDut5Ar+jvjVfDcSRSeywF+VsxB6EEUpHbQNcSe1yMNiJYzsibRH98CbrNgT+jpPVoLGS70fsvPdDynNWOkv9f+YnEXwuF901CkaH/2csplo5Od+r6mS9B3qztC8e9RAVo+n4MbniEMhl2T05TYM5KrLQ9+e61GKv6AldTaTsM8rScWOIfAt6/HofnoxC2H5o08jdkwRVDQGv7NVVnLU7sJWd9sYEHj0WEY2m5kIPpGPW9/RO+xwBHVfrERLCumap0/X/VHMxculmUgu9iRtz97JSEIf1E4Qp7TPyo7lfomA+L2d9+fkjBtFvtW4Cd5yC25e327jc4KnwJ6MNWXxzNy8MjQyWAnHmqFsWlqGpi4OFJfd2Emx1RebNuLFMMWk4X2S+JxwZqJZMOyPuq2KjS1u/bSScg4uv2FgObO2TPD5imMiaxmysqsZvojGkIPXprWRiRNw4OSk97pEq9670UbwO33Yj7pFq6qnQZ7N5HkOptScJ7iAgSqHTiuhPn1g1PYlPS+rNG/3ZCBf/9/lP/ma/ADTE9DZV89i8wAAAABJRU5ErkJggg==\", \"4.conf\": \"W0ludGVyZmFjZV0KQWRkcmVzcyA9IDEwLjAuMC41LzMyClByaXZhdGVLZXkgPSBnSmZTNC9nd2JkMHp3MFA4aGVTSE5scStBeUpKMk0rMFFDOXFnOVI1NG5JPQoKRE5TID0gMS4xLjEuMQoKW1BlZXJdClB1YmxpY0tleSA9IEZCWlFFdUlJZVU0RUVjWFhTOWF4clZWVERvMDNjN2J1UVNWYVB5RzYwd1U9CgpFbmRwb2ludCA9IHdpcmVndWFyZC1zc2gubGlnaHQtc2VhcmNoLmNvbTozODkKQWxsb3dlZElQcyA9IDAuMC4wLjAvMCwgOjovMA==\", \"1.png\": \"iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQMAAAAFsTfpAAAABlBMVEUAAAD///+l2Z/dAAAAAnRSTlP//8i138cAAAAJcEhZcwAACxIAAAsSAdLdfvwAAAOQSURBVFiF7ZhBjqM8EIULsfAOLmCJa3jHlcIFIFwguRI7rmHJF8A7LxD1f056pjWL+aVUbyeKolZ/qHGq6r16tOjfXvKP/C85ROZxuMbYia6bTFvsN2msJOs5bedNUi7pkvapw3Pnl1ay+UnPZU9PjUvxIr7fZfoBWfb2CukKsS+xXvIzMmmre6IYXPJw+iNCDXZZSuzc2ezUFf5dnU8Jf37a/R/v7859THgBm4220CW9j+36PVUfkyOc/dZeEpdNOj5LnDbfW4luQEh7d61qbNR3Y2ysJO9RxmHdY7/r3fmppIdrs5VcY1q1fYQ4128gTYkS7OQY4zy2eW91i+I8+juCn8xE0hH0WaTZk25I2dfpthJV+uNn8bOjRedt5P3VHwM56pEr7EK8BbqUDgbcTvCqeBPO2x4hNqWtd7aSC8mW4RH0wXkFm8FdvJnk7WyKXyjDqFqlDKlCsZF6nw3bGx5jxPaEAQ8pW0lWCqmZARTh1M2WVubISlSHFdlJnPaBz9mdU5HFSg7Blatd0aW+FmDAYLKVXJiBO2/BN+VEbc/Scu1kJXmX2yidG/LONhMZZfm1G02kuhSz3BfGR5/KmMfJTkQcplKtfdqG2q7vU39M8IBczk4wv3PGsQJjOGQrycrOSagk79VEdUt5H1YrORwjwyRSUeQiU9FVfWMmIz0ZdDtngs/LR+/y1pyF5MLsKMp4BGqABNNdvjRnIJfjpBH7lOpYflGy2LvbFoKPEuikfqI/cgo77cv9DUSZGpVeh9eyreFOC/NoJBk70diFsxr8mLSkuzsXKzlG/KldmW5BwfVudTatJOtArLsHROyFu7m2BkYruWqUS/fR3wKLiJ8Ryjs9WQimkpXc+t6NFIBut08rIUogjqVo9b/xJF/c3VtzJlLv43ECyplLDchMYmMl1IDz9vR8Y7rZ3hRVVyuhsbnuxvYhGAPuggUOZsKupiFVtQQovIrSundaNxHFDAgR6cJayClhYI4aK6kZtkZXvjo8Ti+z763kEBzUV81J9fjXhvzSnIGQvJaCH1NXFhGdwbF+ZQoLqaEYwyNNdOEtX+mtpD4zKXkfHb/X42sRWQnPc7MwOGfPbsT5HOtC7KSGax5YB2pA2CGtk2fXH5CpWjuhqW6PvvAc9t6NRjI7/ID1yGG5Sct+y2aimApP1fUxcZazc7+7bSH05+ZQBic9XzdBeb+7/TGx/EfmH/kPvU/TAS6dV7gAAAAASUVORK5CYII=\", \"2.png\": \"iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQMAAAAFsTfpAAAABlBMVEUAAAD///+l2Z/dAAAAAnRSTlP//8i138cAAAAJcEhZcwAACxIAAAsSAdLdfvwAAAOLSURBVFiF7Zg7rus4DIZpqFAXb0CAtqFOW7I34McG7C2p0zYEaAN250Iw56eTg4spZoDDtNcIAsdfEEl8/CRD/F8X/SX/Sw6iIbbJmjNRl9ycSo8bLTm5jdmsWX66ZzeR2TMeaklyQywd+43KRG0g12cavyBjal1qvWy5jRfv35EZu74cjo6bnb8jsAHXM4O3jrEUbv5Y57cE/hmz+9frj+d+TXDdoczMZ4bPYV15zFpyRJrC2zNEAQT2KJ2aWLNFv19mCYT9km395U8t4VzIek40hDYRr7Dr1UY1uSpjEYsH5sx+CWZNvGrJEXDiMgS/EHW5DNFhwV5LsMhGbU7mCGZP8Hw92e964ii2V6jHc/+yZb5o1pIzm5tKz35NcDsOQeP1URcFOWDLDFHxe65bxAlKB7nSkjv4LcLhbbCyyGTrnt420JDzosHSi+SaoQqZcYhRTVK9o4Py7cks5CgQxY91FOSI5UXP49Betm4Wks+7lnDi/SrQJ8jMo3xQl0/OaUgW5TusuPrkMiLh0ieuFeSIvEodgyRIMC4W6lJ3LblxaMJSEjtHbNCqJb5VWUPOC7kLo0JakLv+2fhP7PyecMaWK+IRdXu+GgrjQF+Q5B+BMZuFt90r0sh6gjqGlJ2lMLqR0VmI/q1aIuuQJBzcTmgHkmiVmpwZyYaGwkgkJr/CS2grtIQvz+wgMP31/kqhUEYtwZbJmhtFLMPbdeVHt7TktkhfCAzasTImqAs8/67bGnKyG+DkIAVtEHkuL/vxtoLcljeLT7xe0FSINGLn3T1pyCECajh7iD105YhOqreWID+WwCjXKBfImB49I39yW0GQsjNShOAZg2/tYs02a8kdEcWPjqKHso4sYsewliA5+gvm9CeKdhBHbdZ1aiIZ1lDNxoRahPeCtmJXE/w8iqHoAWIHqoze5yd/FCRDUeqC06OA09No/3RpGiI7NZvEoFSeSWLTqMkRKif0huZGLywDSkWAq8mZ0XzVLUhbDRtsFhncei05pAUoXcbGRQk2a6Qd0xJEMZJuklSjV5THA5ldTySiEdcQvyFAm2Vy6rTkkXYUMSifmy+8w+HUawnmuUFSre4ZfbHMOqiTq5pgcsU8LQ4ndNk3hjDy3xAE8m3riTC09WnYvyJTlDkMqQxvY8RhGENNxAYIZ49EWRCJSLtEaiJzMFbAoMMGvdgUMdv9VNrfE80/Mn/JP4TsrdLoKiS1AAAAAElFTkSuQmCC\", \"4.png\": \"iVBORw0KGgoAAAANSUhEUgAAAMMAAADDAQMAAAAFsTfpAAAABlBMVEUAAAD///+l2Z/dAAAAAnRSTlP//8i138cAAAAJcEhZcwAACxIAAAsSAdLdfvwAAAOLSURBVFiF7ZhBjqMwEEUr8sI7uIAlX8M7XylcAMIF4Ere+RpIvgDsvLCo+UXS0zOLHimV7UTdJOIhTKp+/SqH+KcX/Sf/JDvRxK3P/ow0klnZ9YluWnJwu1s3pHIS3aNZrF8zTmpJciNRZ9udsJSbquszDR+QobYu4ENhxlW8fkZG2wbeOiKyWMd8RLhhnVvawMeI09v0HZ23CfIzZPfX33fm3ibyqnS3SHgbQ5uy+VNV75KdHBEvlnB7BOAReA9l1ZKjlsVuE/OcqSOPLzEGryd5g2r2YJZgzuiXyI9gDjWpfk3ymFyRKF7x7F9VoiFXeh+xzEyjxSLbkNugJWc0XIvUWTY7+TkhDE5NWBTtoEToesrtxmWuhbVkt1iKKHpOfFrPuax1u+lJG61ZInWhHFLBuOpVJQpyksf7aTdJDnJVty76WUt2anfkpJoF8ZAYmAf5VUtkEWpwviE1iq1P0OOXU7xPOIkBQD4zJIMiJlzyqm0F2WPZA+SMyng633aPr++jIEeGtaAFwQnEEsSVk1GTE/WR/BLg9O5aAR7Tei2B7Y1RtLyIRRV41ZyfT60huzXQyygP7vpKt+qg8UNLEIMbe3ShXrKE09AO9WqScNets2LzXWi3LIlSkx0jAIoDqrGui+4mNuNZS6TmEj/InLbB6XF6ZjepiVgLzwk1h6DyEjeiL+1oSOHU4AFHhTfzXKX/HFpyYATIyDPcHUdMUuhsT1fWkN36Bd0sNgowZvi94fyqYAWR3ojmj2qzZo+io91uvZacOBEgFjgBIPIs4Ty0BP+Qc58KgiHjWJCJQE12uTemVzGVh/QfUF61RCZN6+eK20Pa/mHF5llL4KMzOnZEwfkzwKUKjpOWnAH5gfTKVXzSLtbq9AR6yQUFhzBARHN2d2m5SnJU2AAqw1zP7i8r9XqS8Q69IADo2DLcrb9nsfcJ4jdg/I/m0g4mUHx4zjsaAhtgNMYsx5MKlkXT0BOZEw1MZaqoY9jehg7Za4nMhowdGNIiksS+pAvPXY6GMDaaCUOTQSAHaDzKwP4BkTDMsr9pPRojJlA0SS257oodGPXZTbksESLyh5ZgPzdKqWEfhmw3bHSOL7/WkITBBBMiGprEoCPZphyfEHvtluLVOnjr67PTKsmQYE6ojG0kjFHgRU/k9wNsv6Ad2QHAAvvX1Kkhkp8qE8r1w4ZMZGfcei356fWf/Iv8ApNG4r5VQ3npAAAAAElFTkSuQmCC\"}';

    let parsed = Utils.json_loads(data)

    expect(parsed["1.conf"]).toBe("W0ludGVyZmFjZV0KQWRkcmVzcyA9IDEwLjAuMC4yLzMyClByaXZhdGVLZXkgPSBpUE16YkFwRzkwNmpxMnoxRTRyck05YTZ1bVpCVzdYTEE3R1ZGY1VyWmx3PQoKRE5TID0gMS4xLjEuMQoKW1BlZXJdClB1YmxpY0tleSA9IEZCWlFFdUlJZVU0RUVjWFhTOWF4clZWVERvMDNjN2J1UVNWYVB5RzYwd1U9CgpFbmRwb2ludCA9IHdpcmVndWFyZC1zc2gubGlnaHQtc2VhcmNoLmNvbTozODkKQWxsb3dlZElQcyA9IDAuMC4wLjAvMCwgOjovMA==")
  });

  it.only('Testing that json dumping work', async () => {

    let data = {
      abc: "123", bgt: "456"
    }
    let parsed = Utils.json_dumps(data)

    expect(parsed).toBe('{\"abc\":\"123\",\"bgt\":\"456\"}')
  });


  it('tries to initialize installation of the VPN server', async () => {

    // act
    //let response = await Requests.Install({ auth: "ssh", user: "root", ip_address: "wireguard-ssh.light-search.com" })
    let response = await Requests.Install(
      {
        auth: "pass", user: "root", ip_address: "wireguard-pass.light-search.com", password: "test_password_for_pipline_usage"
      }
    )


    // assert
    expect(response.status).toEqual(200)
    expect(response.config.url).toEqual(`${API}/worker/install`)

    var task_id = response.data.task_id

    var status = Requests.STATUS_STATES.pending
    for (var i = 0; i < 999999 && status != Requests.STATUS_STATES.success; i++) {

      var status_response = (await Requests.Status(task_id))
      status = status_response.data.task_id
      await Utils.sleep(5000);
    }

    expect(status).toEqual(Requests.STATUS_STATES.success);

    var configs = (await Requests.Configs(task_id)).data.configs

    expect(configs.includes(".conf")).toBe(true)

  }, 180000 /* Allowed time for test */);

  it('tries to initialize install SSH 22000 VPN server', async () => {

    // act
    //let response = await Requests.Install({ auth: "ssh", user: "root", ip_address: "wireguard-ssh.light-search.com" })
    let response = await Requests.Install(
      {
        auth: "ssh", user: "root", ip_address: "wireguard-ssh.light-search.com", ssh_server_port: "22000"
      }
    )

    // assert
    expect(response.status).toEqual(200)
    expect(response.config.url).toEqual(`${API}/worker/install`)

    var task_id = response.data.task_id

    var status = Requests.STATUS_STATES.pending
    for (var i = 0; i < 999999 && status != Requests.STATUS_STATES.success; i++) {

      var status_response = (await Requests.Status(task_id))
      status = status_response.data.task_id
      await Utils.sleep(5000);
    }

    expect(status).toEqual(Requests.STATUS_STATES.success);

    var configs = (await Requests.Configs(task_id)).data.configs

    expect(configs.includes(".conf")).toBe(true)

  }, 180000 /* Allowed time for test */);
});

describe.only('ignorable tests', () => {
  it.only('not ignores the test', async () => {
    // arrange
    expect(2).toEqual(2);
  });


  it.only('test ', async () => {
    // arrange
    expect(2).toEqual(2);
  });

  it.only('Trying to access object terniary', async () => {
    let task_id_and_status = { task_id: 'f0877e8c-bdb1-4d8a-bc72-5f9aa1a6d46d', status: 'STARTING' }

    let task_id = task_id_and_status.task_id;
    let status = "status" in task_id_and_status ? task_id_and_status.status : "NOT STARTING";

    expect(task_id).toEqual('f0877e8c-bdb1-4d8a-bc72-5f9aa1a6d46d');
    expect(status).toEqual('STARTING');
  });

});




describe.only('specific_tests', () => {
  it.only('specific_test1', async () => {
    // arrange
    expect(2).toEqual(2);
  });
});
