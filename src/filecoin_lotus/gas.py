from filecoin_lotus.rpc_abi import RPC


class Gas:

    def __init__(self, filecoin):
        self._filecoin = filecoin
        self._provider = filecoin.provider

    def estimate_fee_cap(self, message: dict, number: int = 0, tip_set_key: list = None) -> str:
        """
        Estimate fee cap of the message
        :param message
        :param number
        :param tip_set_key : Cid[]
        :return: str
        """
        return self._provider.make_request(RPC.gas_estimateFeeCap, [message, number, tip_set_key])

    def estimate_gas_limit(self, message: dict, tip_set_key: list = None) -> int:
        """
        Estimate gas limit of the message
        :param message
        :param tip_set_key : Cid[]
        :return: int
        """
        return self._provider.make_request(RPC.gas_estimateGasLimit, [message, tip_set_key])
