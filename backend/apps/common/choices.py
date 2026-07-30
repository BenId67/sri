from django.db import models


class DocumentType(models.TextChoices):
    CNIB = "CNIB", "CNIB"
    PASSPORT = "PASSPORT", "Passeport"


class Gender(models.TextChoices):
    MALE = "M", "Masculin"
    FEMALE = "F", "Féminin"



class VisitStatus(models.TextChoices):
    CREATED = "CREATED", "Créée"
    IN_PROGRESS = "IN_PROGRESS", "En cours"
    COMPLETED = "COMPLETED", "Terminée"
    CANCELLED = "CANCELLED", "Annulée"


class AuditAction(models.TextChoices):
    LOGIN = "LOGIN", "Connexion"
    LOGOUT = "LOGOUT", "Déconnexion"

    CREATE = "CREATE", "Création"
    UPDATE = "UPDATE", "Modification"
    DELETE = "DELETE", "Suppression"

    CREATE_VISIT = "CREATE_VISIT", "Création d'une visite"
    VALIDATE_CHECKPOINT = "VALIDATE_CHECKPOINT", "Validation d'un poste"

    GENERATE_QR_CODE = "GENERATE_QR_CODE", "Génération du QR Code"
    SCAN_QR_CODE = "SCAN_QR_CODE", "Scan du QR Code"

    ISSUE_BADGE = "ISSUE_BADGE", "Remise du badge"
    RETURN_BADGE = "RETURN_BADGE", "Retour du badge"

    RETAIN_DOCUMENT = "RETAIN_DOCUMENT", "Consignation de la pièce"
    RETURN_DOCUMENT = "RETURN_DOCUMENT", "Restitution de la pièce"

    COMPLETE_VISIT = "COMPLETE_VISIT", "Fin de la visite"

    ACTIVATE_USER = "ACTIVATE_USER", "Activation d'un utilisateur"
    DEACTIVATE_USER = "DEACTIVATE_USER", "Désactivation d'un utilisateur"


class AuditEntity(models.TextChoices):
    USER = "USER", "Utilisateur"
    ROLE = "ROLE", "Rôle"

    VISITOR = "VISITOR", "Visiteur"
    VISIT = "VISIT", "Visite"

    WORKFLOW = "WORKFLOW", "Workflow"
    WORKFLOW_STEP = "WORKFLOW_STEP", "Étape du workflow"

    CHECKPOINT = "CHECKPOINT", "Poste de contrôle"

    QR_CODE = "QR_CODE", "QR Code"

    BADGE = "BADGE", "Badge"