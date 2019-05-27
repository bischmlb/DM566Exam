#Exercise 4-1\

Support threshold = 2

| TransID | Items |
|---------|-------|
| A       | 6     |
| B       | 6     |
| C       | 7     |
| D       | 5     |
| E       | 6     |
| F       | 3     | \

| TransID | Items |
|---------|-------|
| AB      | 4     |
| AC      | 4     |
| AD      | 2     |
| AE      | 4     |
| AF      | 1     |
| BC      | 4     |
| BD      | 4     |
| BE      | 4     |
| BF      | 2     |
| CD      | 3     |
| CE      | 5     |
| CF      | 3     |
| DE      | 1     |
| DF      | 2     |
| EF      | 1     |\

Her fjerner vi altså AF, DE, EF fordi de er under 2:

| TransID | Items |
|---------|-------|
| AB      | 4     |
| AC      | 4     |
| AD      | 2     |
| AE      | 4     |
| BC      | 4     |
| BD      | 4     |
| BE      | 4     |
| BF      | 2     |
| CD      | 3     |
| CE      | 5     |
| CF      | 3     |
| DF      | 2     |\

| TransID | Items |
|---------|-------|
| ABC     | 2     |
| ABD     | 2     |
| ABE     | 2     |
| ACD     | 1     |
| ACE     | 3     |
| ADE     | 0     |
| BCD     | 2     |
| BCE     | 3     |
| BCF     | 2     |
| BDE     | 1     |
| BDF     | 1     |
| BEF     | 1     |
| CDE     | 1     |
| CDF     | 2     |
| CEF     | 1     |\
Nu fjerner vi ACD, ADE, BDE, BDF, BEF, CDE, CEF

**| TransID | Items |
|---------|-------|
| ABC     | 2     |
| ABD     | 2     |
| ABE     | 2     |
| ACE     | 3     |
| BCD     | 2     |
| BCE     | 3     |
| BCF     | 2     |
| CDF     | 2     |**\

| TransID | Items |
|---------|-------|
| ABCD    | 1     |
| ABCE    | 1     |
| ABDE    | 0     |
| BCDE    | 1     |
| BCDF    | 1     |
| BCEF    | 1     |\

Her skal alle fjernes, og tabellen er derfor irrelevant. Vi bruger forrige.\

Result: ABC, ABD, ABE, ACE, BCD, BCE, BCF, CDF
