import logging
import asyncio
import grpc
from card_pb2 import Card, CreateCardResponse, GetCardsResponse
from card_pb2_grpc import CardServiceServicer, add_CardServiceServicer_to_server


class CardService(CardServiceServicer):

    pokemonCards = []
    currentId = 1

    async def CreateCard(self, request, context):
        card = Card(id=self.currentId, name='Example Card')
        self.pokemonCards.append(card);
        self.currentId += 1
        return CreateCardResponse(card=card)

    async def GetCards(self, request, context):
        return GetCardsResponse(cards=self.pokemonCards)


async def serve() -> None:
    server = grpc.aio.server()
    add_CardServiceServicer_to_server(CardService(), server)
    listen_addr = '[::]:50051'
    server.add_insecure_port(listen_addr)
    logging.info("Starting server on %s", listen_addr)
    await server.start()
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(serve())
