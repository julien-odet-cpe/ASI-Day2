import asyncio
import logging
import grpc
from card_pb2 import CreateCardRequest, GetCardsRequest
from card_pb2_grpc import CardServiceStub

async def run() -> None:
    async with grpc.aio.insecure_channel('localhost:50051') as channel:
        stub = CardServiceStub(channel)

        # Appeler la méthode CreateCard plusieurs fois
        for _ in range(3):
            request = CreateCardRequest()
            response = await stub.CreateCard(request)
            print("Created card:", response.card)

        # Appeler la méthode GetCards
        request = GetCardsRequest()
        response = await stub.GetCards(request)
        print("All cards:", response.cards)


if __name__ == '__main__':
    logging.basicConfig()
    asyncio.run(run())
