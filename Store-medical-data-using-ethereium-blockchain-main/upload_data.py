from web3 import Web3
import json
class check:
    def check_data(data_type,address1,public_key,index):
        # Set up web3 connection with Ganache
        ganache_url = "http://127.0.0.1:5000"
        web3= Web3(Web3.HTTPProvider(ganache_url))
                
        with open('smartcontract.json') as json_file:
            abi = json.load(json_file)
        bytecode="60606040526220f580600655341561001657600080fd5b5b612007806100266000396000f300606060405236156100e3576000357c0100000000000000000000000000000000000000000000000000000000900463ffffffff168062774aa2146100e85780631b6e23ea146101355780633d1d0fae146101825780634d15a9bb146102785780634e6bd1c0146102d257806364148056146103c857806372f70000146104da578063a346a9c6146105ec578063c45d9bea146106e2578063ce3e8d84146107f4578063d1fbd84014610870578063de6f24bb146108ec578063e0c01bfe14610968578063ea953b1214610a55578063edc8f0d814610aa2578063f1703b9114610aef575b600080fd5b34156100f357600080fd5b61011f600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610b18565b6040518082815260200191505060405180910390f35b341561014057600080fd5b61016c600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050610b30565b6040518082815260200191505060405180910390f35b341561018d57600080fd5b6101c2600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091908035906020019091905050610b48565b604051808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200180602001838152602001828103825284818151815260200191508051906020019080838360005b8381101561023b5780820151818401525b60208101905061021f565b50505050905090810190601f1680156102685780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b341561028357600080fd5b6102b8600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091908035906020019091905050610d22565b604051808215151515815260200191505060405180910390f35b34156102dd57600080fd5b610312600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091908035906020019091905050610d87565b604051808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200180602001838152602001828103825284818151815260200191508051906020019080838360005b8381101561038b5780820151818401525b60208101905061036f565b50505050905090810190601f1680156103b85780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b34156103d357600080fd5b610408600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091908035906020019091905050610f61565b604051808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001806020018381526020018281038252848181546001816001161561010002031660029004815260200191508054600181600116156101000203166002900480156104c95780601f1061049e576101008083540402835291602001916104c9565b820191906000526020600020905b8154815290600101906020018083116104ac57829003601f168201915b505094505050505060405180910390f35b34156104e557600080fd5b61051a600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091908035906020019091905050610fb7565b604051808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001806020018381526020018281038252848181546001816001161561010002031660029004815260200191508054600181600116156101000203166002900480156105db5780601f106105b0576101008083540402835291602001916105db565b820191906000526020600020905b8154815290600101906020018083116105be57829003601f168201915b505094505050505060405180910390f35b34156105f757600080fd5b61062c600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001909190505061100d565b604051808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200180602001838152602001828103825284818151815260200191508051906020019080838360005b838110156106a55780820151818401525b602081019050610689565b50505050905090810190601f1680156106d25780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b34156106ed57600080fd5b610722600480803573ffffffffffffffffffffffffffffffffffffffff169060200190919080359060200190919050506111e7565b604051808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001806020018381526020018281038252848181546001816001161561010002031660029004815260200191508054600181600116156101000203166002900480156107e35780601f106107b8576101008083540402835291602001916107e3565b820191906000526020600020905b8154815290600101906020018083116107c657829003601f168201915b505094505050505060405180910390f35b34156107ff57600080fd5b61086e600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001908201803590602001908080601f0160208091040260200160405190810160405280939291908181526020018383808284378201915050505050509190505061123d565b005b341561087b57600080fd5b6108ea600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001908201803590602001908080601f01602080910402602001604051908101604052809392919081815260200183838082843782019150505050505091905050611573565b005b34156108f757600080fd5b610966600480803573ffffffffffffffffffffffffffffffffffffffff1690602001909190803590602001908201803590602001908080601f016020809104026020016040519081016040528093929190818152602001838380828437820191505050505050919050506118a9565b005b341561097357600080fd5b61099f600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050611bdb565b604051808473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200180602001838152602001828103825284818151815260200191508051906020019080838360005b83811015610a185780820151818401525b6020810190506109fc565b50505050905090810190601f168015610a455780820380516001836020036101000a031916815260200191505b5094505050505060405180910390f35b3415610a6057600080fd5b610a8c600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050611ebb565b6040518082815260200191505060405180910390f35b3415610aad57600080fd5b610ad9600480803573ffffffffffffffffffffffffffffffffffffffff16906020019091905050611ed3565b6040518082815260200191505060405180910390f35b3415610afa57600080fd5b610b02611f1c565b6040518082815260200191505060405180910390f35b60016020528060005260406000206000915090505481565b60006020528060005260406000206000915090505481565b6000610b52611f22565b6000600460008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600060018603815260200190815260200160002060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16600460008773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000600187038152602001908152602001600020600101600460008873ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600060018803815260200190815260200160002060020154818054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610d0d5780601f10610ce257610100808354040283529160200191610d0d565b820191906000526020600020905b815481529060010190602001808311610cf057829003601f168201915b505050505091509250925092505b9250925092565b600042600654600360008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600085815260200190815260200160002060020154011190505b92915050565b6000610d91611f22565b6000600360008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600060018603815260200190815260200160002060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16600360008773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000600187038152602001908152602001600020600101600360008873ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600060018803815260200190815260200160002060020154818054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015610f4c5780601f10610f2157610100808354040283529160200191610f4c565b820191906000526020600020905b815481529060010190602001808311610f2f57829003601f168201915b505050505091509250925092505b9250925092565b6004602052816000526040600020602052806000526040600020600091509150508060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169080600101908060020154905083565b6005602052816000526040600020602052806000526040600020600091509150508060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169080600101908060020154905083565b6000611017611f22565b6000600560008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600060018603815260200190815260200160002060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16600560008773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000600187038152602001908152602001600020600101600560008873ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600060018803815260200190815260200160002060020154818054600181600116156101000203166002900480601f0160208091040260200160405190810160405280929190818152602001828054600181600116156101000203166002900480156111d25780601f106111a7576101008083540402835291602001916111d2565b820191906000526020600020905b8154815290600101906020018083116111b557829003601f168201915b505050505091509250925092505b9250925092565b6003602052816000526040600020602052806000526040600020600091509150508060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff169080600101908060020154905083565b33600460008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000600160008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054815260200190815260200160002060000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555080600460008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000600160008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054815260200190815260200160002060010190805190602001906113b4929190611f36565b5042600460008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000600160008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054815260200190815260200160002060020181905550600160008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600081548092919060010191905055508173ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167fdd99aef5e4fdfad84059320be40f5dc0f015dc4025f56bd4010608c6743bc22e42846040518083815260200180602001828103825283818151815260200191508051906020019080838360005b838110156115335780820151818401525b602081019050611517565b50505050905090810190601f1680156115605780820380516001836020036101000a031916815260200191505b50935050505060405180910390a35b5050565b33600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000600260008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054815260200190815260200160002060000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555080600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000600260008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054815260200190815260200160002060010190805190602001906116ea929190611f36565b5042600560008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000206000600260008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054815260200190815260200160002060020181905550600260008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600081548092919060010191905055508173ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167fdd99aef5e4fdfad84059320be40f5dc0f015dc4025f56bd4010608c6743bc22e42846040518083815260200180602001828103825283818151815260200191508051906020019080838360005b838110156118695780820151818401525b60208101905061184d565b50505050905090810190601f1680156118965780820380516001836020036101000a031916815260200191505b50935050505060405180910390a35b5050565b33600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008060008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054815260200190815260200160002060000160006101000a81548173ffffffffffffffffffffffffffffffffffffffff021916908373ffffffffffffffffffffffffffffffffffffffff16021790555080600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008060008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205481526020019081526020016000206001019080519060200190611a1e929190611f36565b5042600360008473ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002060008060008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020548152602001908152602001600020600201819055506000808373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600081548092919060010191905055508173ffffffffffffffffffffffffffffffffffffffff163373ffffffffffffffffffffffffffffffffffffffff167fdd99aef5e4fdfad84059320be40f5dc0f015dc4025f56bd4010608c6743bc22e42846040518083815260200180602001828103825283818151815260200191508051906020019080838360005b83811015611b9b5780820151818401525b602081019050611b7f565b50505050905090810190601f168015611bc85780820380516001836020036101000a031916815260200191505b50935050505060405180910390a35b5050565b6000611be5611f22565b6000806000808673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054111515611c3357600080fd5b600360008573ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600060016000808873ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205403815260200190815260200160002060000160009054906101000a900473ffffffffffffffffffffffffffffffffffffffff16600360008673ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600060016000808973ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff16815260200190815260200160002054038152602001908152602001600020600101600360008773ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff168152602001908152602001600020600060016000808a73ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205403815260200190815260200160002060020154818054600181600116156101000203166002900480601f016020809104026020016040519081016040528092919081815260200182805460018160011615610100020316600290048015611ea65780601f10611e7b57610100808354040283529160200191611ea6565b820191906000526020600020905b815481529060010190602001808311611e8957829003601f168201915b505050505091509250925092505b9193909250565b60026020528060005260406000206000915090505481565b60008060008373ffffffffffffffffffffffffffffffffffffffff1673ffffffffffffffffffffffffffffffffffffffff1681526020019081526020016000205490505b919050565b60065481565b602060405190810160405280600081525090565b828054600181600116156101000203166002900490600052602060002090601f016020900481019282601f10611f7757805160ff1916838001178555611fa5565b82800160010185558215611fa5579182015b82811115611fa4578251825591602001919060010190611f89565b5b509050611fb29190611fb6565b5090565b611fd891905b80821115611fd4576000816000905550600101611fbc565b5090565b905600a165627a7a7230582094fb20ef414f20e9f762ad73d79d58898557f9b0057ac61f446e6dfa91ad13d50029"
                	
                # set pre-funded account as sender
                
                # Create the contract instance with the newly-deployed address
        contract = web3.eth.contract(
           address=address1,
           abi=abi,
        )
        if data_type=="Lab":
            datasend=contract.functions.getlabByIndex(public_key,index).call()
        if data_type=="prescription":
            datasend=contract.functions.getprescriptonByIndex(public_key,index).call()
        return datasend
    def data_upload(contract,data_type,public_key,data):
        if data_type=='Lab':
            contract.functions.Lab(public_key,data).transact()
        elif data_type=='prescription':
           contract.functions.Prescription(public_key,data).transact()
        else:
            None
        