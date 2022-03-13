## Inspiration 👨🏻‍💻
Since we are heading to Web3 era, and the generic shopping apps don't use blockchain ,so we thought of making a dApp for shopping using python, java, and hedera. We made this hack as we saw the growing market in Web3 and we wanted to use hedera because its 3rd generation public ledger and this hackathon was the right place and idea to implement the project.

## What it does 🔖

Our app basically is a shopping app where it uses **Hedera's HBAR** as currency and hashgraph as it's database, so the whole thing is stored in blockchain. You can buy products here with HBAR which is on Hedera Testnet as of now. 
- First, you have to create an account, which will be created in Hashgraph, after creating an account it will automatically sign you in, then every account will have 1000 HBAR(currency), 
- then head over to cart section in sidebar 
- then their you can find denominations of HBAR and can buy the products from the page, 
- the respective amount will get deducted along with the transaction fee and will be redirected to the account page where we can see the remaining amount along with what we bought and its price in tinybars.

## How we built it 🌀
We used python framework and Java SDK to make our app. We made the app work on tinybars specifically because with that we can be more accurate about how much the product is sold for. hedera-sdk-py was very much help it led us use JAVA SDK in python and both Hedera's and hedera-sdk-py documentations were of very great help.

## Challenges we ran into 🏃🏻
Java was new to us and Hedera itself was new. We initially had a broad plan and wanted every single detail of our project to be functional but the time constraint and lack of technical soundness in some aspects led to last-minute complications.

## Accomplishments that we're proud of 🏆
We are proud that we could pull up the hack in time less than we expected it it to take. We were able to make the payments down to tinybars(smallest denomination) for transactions. We came across multiple issues throughout the project but we are very happy with the product we could assemble in a short duration, we are happy that the majority of our hack is functional. What we thought at the start, we were able to complete it by the end.

## What we learned 🧾
We learnt a lot about **Hedera** and **JAVA SDK**. Apart from subjective and practical gains from the project we were able to pinpoint how important coordinating within is, we learnt that matching the energy and productivity rate with the rest of the team is very essential.

## What's next for CRYPT-O-PPING ⏭️
Since for the hack we were supposed to use Testnet, we will be shifting the dApp to Mainnet after adding more features. Then we will release it to public use and we will update it frequently as we get updates from Hedera JAVA SDK or hedera-sdk-py.
